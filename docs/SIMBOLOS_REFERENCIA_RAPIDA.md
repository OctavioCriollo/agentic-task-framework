# Referencia Rápida: Simbología Permitida v3.1

**Fuente autoritativa:** CLAUDE.md:71-309
**Versión:** v3.1 Master (2026-01-18)

---

## Regla de Oro

**Funcional SÍ, Decorativo NO**

Si el símbolo sirve para indicar estado, estructura o dirección: PERMITIDO
Si el símbolo es decorativo o pictográfico: PROHIBIDO

---

## Permitidos por Categoría

### Status
- ✓ ✅ ✗ ❌ (checkmarks/X-marks)
- 🟡 🟢 🔴 🟠 (status circles)

### Estructura
- ⚪ ⚫ 🔘 ● (radio/bullets)
- Rango completo U+2500-U+257F (box-drawing)

### Dirección
- ← → ↑ ↓ ↔ ↕ (arrows)

### Énfasis (uso mínimo)
- ⚠️ (warning)
- ⚡ (priority)
- ❓ (unclear)
- ☆ ★ (ratings only)

---

## Prohibidos Siempre

- 😊 😀 🤔 (faces)
- 📁 💻 📊 🚀 (objects)
- 🎉 🏆 🎁 (celebrations)
- 👍 👎 🙏 (gestures)
- ❤️ 💙 ✨ (decorative)

---

## Alternativas Texto Plano

Siempre aceptables:

```
✅ → COMPLETED:
❌ → ERROR:
⚠️ → WARNING:
🟡 → IN_PROGRESS:
🟢 → SUCCESS:
🔴 → FAILED:
🟠 → ATTENTION:
```

---

## Cuándo Usar Símbolos vs Texto

**USA SÍMBOLOS:**
- Dashboards visuales
- Listas de tareas
- Status rápido
- Diagramas estructurales

**USA TEXTO PLANO:**
- Logs para parsing
- Scripts automatizados
- Entornos sin Unicode
- Accesibilidad crítica

---

## Scripts de Validación

```bash
# Escanear símbolos prohibidos
python -m scripts.verificar_simbolos_no_permitidos

# Limpiar emojis prohibidos (usa con cuidado)
python -m scripts.limpiar_emojis

# Auditar uso de símbolos
python -m scripts.encontrar_simbolos
```

**NOTA:** scripts/limpiar_emojis.py tiene bugs conocidos (pendiente corrección v3.1).

---

## FAQ Rápido

**Q: ¿Puedo usar 🐍 para Python?**
A: NO. Usa "Python:" o sin símbolo.

**Q: ¿Puedo usar 📝 para notas?**
A: NO. Usa "NOTE:" o "NOTA:".

**Q: ¿Box-drawing doble ╔╗╚╝ permitido?**
A: SÍ. Toda la categoría U+2500-U+257F está permitida.

**Q: ¿Cuántas estrellas ★ puedo usar?**
A: Solo para ratings (★★★☆☆). No para decoración.

**Q: ¿Dónde está la lista completa?**
A: CLAUDE.md líneas 71-309.

---

## Jerarquía de Autoridad

1. **CLAUDE.md:71-309** (MÁXIMA)
2. Scripts de validación
3. Otros documentos

En caso de conflicto, CLAUDE.md gana siempre.

---

**Última actualización:** 2026-01-18
**Próxima revisión:** Según necesidad (consultar maintainer)
