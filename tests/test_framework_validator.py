"""
Tests for FrameworkValidator class.
"""

import pytest
from pathlib import Path
from core.framework_validator import FrameworkValidator


# Helper function to create valid base prompt
def create_base_prompt_with_separator():
    """Create a base prompt that includes the separator."""
    return """# Test Task

## Layer 1: Conversational Context

The user has requested testing of the framework's prompt validation system.
This is a controlled test environment for validating security features.

**Context:**
- Test environment for security validation
- Supervised test execution
- Academic testing framework
- No real-world impact on production systems

**User Request:**
Validate that the framework properly enforces the separator requirement
between Layer 1 (conversational context) and Layer 2 (technical details).

This ensures agents receive proper context before technical instructions.

---

## Layer 2: Technical Task

**Objective:** Validate separator enforcement in prompt architecture

**Methodology:**
1. Submit test prompts with and without separators
2. Framework validator processes each prompt
3. Verify correct validation results
4. Confirm error messages are clear

**Expected Outputs:**
- Validation passes for prompts with separator
- Validation fails for prompts without separator
- Clear, actionable error messages

**Success Criteria:**
- Separator requirement enforced correctly
- No false positives or negatives
- Framework prevents malformed prompts
"""


class TestPromptSeparatorValidation:
    """Test suite for '---' separator validation (SECURITY FIX H1)."""

    def test_reject_prompt_without_separator(self, temp_projects_dir):
        """Reject prompts missing '---' separator."""
        validator = FrameworkValidator(temp_projects_dir.parent)

        # Get base prompt and remove the separator
        prompt_no_separator = create_base_prompt_with_separator().replace('\n---\n', '\n\n')

        result = validator._validate_prompt_architecture(prompt_no_separator)

        assert not result["valid"]
        assert "Missing '---' separator" in result["reason"]

    def test_accept_prompt_with_separator(self, temp_projects_dir):
        """Accept prompts with correct '---' separator."""
        validator = FrameworkValidator(temp_projects_dir.parent)

        prompt_with_separator = create_base_prompt_with_separator()

        result = validator._validate_prompt_architecture(prompt_with_separator)

        assert result["valid"], f"Expected valid, got: {result['reason']}"

    def test_accept_prompt_with_multiple_dashes(self, temp_projects_dir):
        """Accept prompts with multiple dashes (----, -----, etc.)."""
        validator = FrameworkValidator(temp_projects_dir.parent)

        # Replace separator with longer dash sequence
        prompt_with_many_dashes = create_base_prompt_with_separator().replace('\n---\n', '\n-------\n')

        result = validator._validate_prompt_architecture(prompt_with_many_dashes)

        assert result["valid"], f"Expected valid, got: {result['reason']}"

    def test_accept_separator_with_whitespace(self, temp_projects_dir):
        """Accept separator with surrounding whitespace."""
        validator = FrameworkValidator(temp_projects_dir.parent)

        # Add whitespace around separator
        prompt_whitespace = create_base_prompt_with_separator().replace('\n---\n', '\n   ---   \n')

        result = validator._validate_prompt_architecture(prompt_whitespace)

        assert result["valid"], f"Expected valid, got: {result['reason']}"

    def test_reject_partial_separator(self, temp_projects_dir):
        """Reject prompts with incomplete separator (-- instead of ---)."""
        validator = FrameworkValidator(temp_projects_dir.parent)

        # Replace separator with only 2 dashes
        prompt_incomplete = create_base_prompt_with_separator().replace('\n---\n', '\n--\n')

        result = validator._validate_prompt_architecture(prompt_incomplete)

        assert not result["valid"]
        assert "Missing '---' separator" in result["reason"]


class TestPromptArchitectureValidation:
    """Test suite for general prompt architecture validation."""

    def test_reject_too_short_prompt(self, temp_projects_dir):
        """Reject prompts shorter than 500 characters."""
        validator = FrameworkValidator(temp_projects_dir.parent)

        short_prompt = "This is too short"

        result = validator._validate_prompt_architecture(short_prompt)

        assert not result["valid"]
        assert "too short" in result["reason"].lower()

    def test_reject_prompt_without_sections(self, temp_projects_dir):
        """Reject prompts without proper section headers."""
        validator = FrameworkValidator(temp_projects_dir.parent)

        # Long prompt but no section headers
        no_sections = "A" * 600 + "\n---\n" + "B" * 600

        result = validator._validate_prompt_architecture(no_sections)

        assert not result["valid"]

    def test_accept_valid_bilingual_prompt(self, temp_projects_dir):
        """Accept valid prompts in Spanish/English."""
        validator = FrameworkValidator(temp_projects_dir.parent)

        bilingual_prompt = """# Tarea de Prueba

## Capa 1: Contexto Conversacional

El usuario ha solicitado una investigacion de prueba del framework.
Este es un entorno controlado para validar funcionalidad de seguridad.

**Contexto:**
- Entorno de prueba controlado
- Ejecucion supervisada
- Marco de pruebas academico
- Sin impacto en sistemas de produccion

**Solicitud del Usuario:**
Validar que el framework aplique correctamente el requisito del separador
entre la Capa 1 (contexto conversacional) y Capa 2 (detalles tecnicos).

Esto asegura que los agentes reciban contexto apropiado antes de instrucciones.

---

## Capa 2: Tarea Tecnica

**Objetivo:** Validar aplicacion del separador en arquitectura de prompts

**Metodologia:**
1. Enviar prompts de prueba con y sin separadores
2. El validador del framework procesa cada prompt
3. Verificar resultados de validacion correctos
4. Confirmar que mensajes de error son claros

**Salidas Esperadas:**
- Validacion exitosa para prompts con separador
- Validacion fallida para prompts sin separador
- Mensajes de error claros y accionables

**Criterios de Exito:**
- Requisito de separador aplicado correctamente
- Sin falsos positivos ni negativos
- Framework previene prompts malformados
"""

        result = validator._validate_prompt_architecture(bilingual_prompt)

        assert result["valid"], f"Expected valid, got: {result['reason']}"

    def test_reject_missing_layer1_keywords(self, temp_projects_dir):
        """Reject prompts missing Layer 1 context keywords."""
        validator = FrameworkValidator(temp_projects_dir.parent)

        # Prompt with separator but no Layer 1 keywords
        no_layer1 = """# Test

## Section One

This is just random content without proper context markers.
No user request, no context, no disclaimers.
Just filler text to meet length requirements.
More filler text here.
And more text.
Even more text to reach minimum length.

---

## Layer 2: Task

**Objective:** Test validation

**Methodology:**
1. Submit prompt without Layer 1 markers
2. Verify validation fails
3. Check error message

**Expected Outputs:**
- Validation should fail
- Error about missing Layer 1

**Success Criteria:**
- Proper Layer 1 required
- Clear error messages
"""

        result = validator._validate_prompt_architecture(no_layer1)

        assert not result["valid"]
        assert "Layer 1" in result["reason"]

    def test_reject_missing_layer2_keywords(self, temp_projects_dir):
        """Reject prompts missing Layer 2 technical keywords."""
        validator = FrameworkValidator(temp_projects_dir.parent)

        # Prompt with separator but no Layer 2 keywords
        no_layer2 = """# Test

## Layer 1: Context

User requested validation testing of framework security features.

**Context:**
- Test environment
- Supervised execution
- No production impact

This validates that Layer 2 technical markers are required.

---

## Section Two

This is just random content without proper technical markers.
No objective, no methodology, no deliverables.
Just filler text to meet length requirements.
More filler text here.
And more text.
Even more text to reach minimum length for this section.
"""

        result = validator._validate_prompt_architecture(no_layer2)

        assert not result["valid"]
        assert "Layer 2" in result["reason"]
