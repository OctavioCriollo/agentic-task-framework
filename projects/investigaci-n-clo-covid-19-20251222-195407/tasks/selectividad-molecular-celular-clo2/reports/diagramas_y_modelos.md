# DIAGRAMAS Y MODELOS VISUALES: SELECTIVIDAD DE ClO₂

## CONTENIDO

1. [Modelo de Competencia Molecular](#modelo-de-competencia-molecular)
2. [Escenarios de Selectividad](#escenarios-de-selectividad)
3. [Pathway Integrado Multi-Etapa](#pathway-integrado-multi-etapa)
4. [Árbol de Decisión: Investigación](#árbol-de-decisión-investigación)
5. [Comparación con Antivirales](#comparación-con-antivirales)

---

## MODELO DE COMPETENCIA MOLECULAR

### Diagrama 1: Distribución de ClO₂ en Célula Infectada

```
┌─────────────────────────────────────────────────────────────┐
│ CÉLULA INFECTADA │
│ │
│ [ClO₂] entra (100 μM) │
│ -> │
│ ┌────┴─────┐ │
│ │ │ │
│ -> -> │
│ GSH Proteínas │
│ (2 mM) (~100 μM tioles) │
│ 99% 1% │
│ -> -> │
│ GSSG ┌────┴─────┐ │
│ │ │ │
│ -> -> │
│ Humanas Virales │
│ (1M tioles) (11k tioles) │
│ 98.9% 1.1% │
│ │
│ CONCLUSIÓN: │
│ De 100 μM ClO₂: │
│ - 99 μM → GSH │
│ - 0.989 μM → Proteínas humanas │
│ - 0.011 μM → Proteínas virales │
│ │
│ Ratio oxidación: Humana/Viral = 90:1 │
│ SELECTIVIDAD: NINGUNA (favorece oxidación humana) │
└─────────────────────────────────────────────────────────────┘
```

### Diagrama 2: Cinética de Oxidación (Constantes de Velocidad)

```
REACTIVIDAD DE ClO₂ CON DIFERENTES TARGETS
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Target k (M⁻¹s⁻¹) Reactividad
─────────────────────────────────────────────────────────

Tiol libre (Cys-SH) 10⁶ - 10⁷ ████████████ MUY ALTA
 ├─ Citoplasmático 10⁶ - 10⁷ ████████████
 ├─ Spike (si expuesto) 10⁵ - 10⁶ ██████████
 └─ GSH 10⁶ ████████████

Puente disulfuro (S-S) 10³ ███ BAJA
 └─ Spike protein 10³ - 10⁴ ███

Triptófano (Trp) 10⁴ - 10⁵ ████████ ALTA

Tirosina (Tyr) 10³ - 10⁴ █████ MODERADA

Metionina (Met) 10³ - 10⁴ █████ MODERADA

─────────────────────────────────────────────────────────

CONCLUSIÓN: No hay diferencia sistemática entre viral vs humano.
 Reactividad depende de ESTADO QUÍMICO (tiol libre vs S-S),
 NO de origen (viral vs humano).
```

### Diagrama 3: Energía Libre de Oxidación (Termodinámica)

```
PERFIL TERMODINÁMICO DE OXIDACIÓN
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

 ΔG°' (kJ/mol)
 -100 -50 0
 │ │ │
Cys viral (spike) ├──────● │
 │ ↕ 0-5 │
Cys humano (ACE2) ├──────● │
 │ │
Cys-SH + ClO₂ │ │
 -> │ │
Cys-SO₂H + ClO⁻ │ │
 │ │
ESPONTÁNEO ←──────────────┤ │

ΔG°' viral ≈ ΔG°' humano ± 5 kJ/mol

CONCLUSIÓN: No hay preferencia termodinámica por proteínas virales.
 Ambas son igualmente oxidables (dentro del error experimental).
```

---

## ESCENARIOS DE SELECTIVIDAD

### Escenario A: Selectividad Espacial (Extracelular)

```
TIEMPO: 0-5 minutos tras exposición
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

 ESPACIO EXTRACELULAR (Alveolo / Sangre)
┌──────────────────────────────────────────────────────────┐
│ │
│ [ClO₂] = 10 μM │
│ │
│ ○ ← Virión libre │
│ ╱│╲ (Spike 100% expuesto) │
│ ○ ○ ○ Oxidación RÁPIDA │
│ │
│ - - - - - - - - - - ← Célula sana │
│ | | (Membrana protege interior) │
│ | [ClO₂] | ClO₂ penetra lentamente (t₁/₂ ~30s) │
│ | = 2 μM | │
│ - - - - - - - - - - Exposición REDUCIDA (temporal) │
│ │
└──────────────────────────────────────────────────────────┘

SELECTIVIDAD TEMPORAL:
- 0-1 min: Virus expuesto a 10 μM, Células a 2 μM → Ratio 5:1
- 1-5 min: Virus expuesto a 5 μM, Células a 4 μM → Ratio 1.25:1
- >5 min: Equilibrio completo → Ratio 1:1

FACTOR DE SELECTIVIDAD: 1.5-2× (INSUFICIENTE)

LIMITACIÓN:
- Ventana temporal MUY CORTA (<5 min)
- Penetración celular es RÁPIDA (ClO₂ es pequeño, apolar)
- No hay barrera efectiva de membrana
```

### Escenario B: Selectividad por GSH Bajo

```
ESTADO REDOX DIFERENCIAL
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

CÉLULA SANA CÉLULA INFECTADA
┌─────────────────────┐ ┌─────────────────────┐
│ │ │ │
│ [GSH] = 5 mM │ │ [GSH] = 1.5 mM │
│ (PROTECCIÓN ALTA) │ │ (PROTECCIÓN BAJA) │
│ │ │ │
│ ClO₂ (100 μM) │ │ ClO₂ (100 μM) │
│ -> │ │ -> │
│ 99% → GSH │ │ 95% → GSH │
│ 1% → Proteínas │ │ 5% → Proteínas │
│ │ │ │
│ Daño: 2% │ │ Daño: 6% │
│ VIABLE ✓ │ │ VULNERABLE ✗ │
│ │ │ │
└─────────────────────┘ └─────────────────────┘

FACTOR DE SELECTIVIDAD: 3× (6% / 2%)

EVALUACIÓN:
- Factor 3× es MEJOR que nada
- Pero INSUFICIENTE para ventana terapéutica amplia
 (Requiere >10× para seguridad clínica)

- COMPLEMENTARIO con otros mecanismos
- Dependiente de:
 * Nivel de infección (GSH más bajo en infección severa)
 * Estado nutricional (Cys, NAC disponibilidad)
 * Capacidad de regeneración (NADPH, glutatión reductasa)
```

### Escenario C: Conversión a HOCl en Neutrófilos

```
MECANISMO INMUNE: FAGOCITOSIS Y OXIDACIÓN COMPARTIMENTALIZADA
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

PASO 1: ClO₂ → ClO⁻ (clorito) en plasma
──────────────────────────────────────
 ClO₂ + e⁻ → ClO₂⁻ (reducción parcial)

PASO 2: Fagocitosis de virus/células infectadas
──────────────────────────────────────────────

 NEUTRÓFILO
 ┌───────────────────────────────────────┐
 │ │
 │ FAGOLISOSOMA │
 │ ┌──────────────────┐ │
 │ │ │ │
 │ │ ○ ← Virus │ │
 │ │ │ │
 │ │ [HOCl] = 5 mM │ ← Concentración LETAL
 │ │ │ │
 │ │ DESTRUCCIÓN │ │
 │ │ │ │
 │ └──────────────────┘ │
 │ │
 │ CITOPLASMA (protegido) │
 │ - Catalasa, SOD │
 │ - Membranas resistentes │
 │ │
 └───────────────────────────────────────┘

PASO 3: Generación de HOCl
──────────────────────────
 MPO (mieloperoxidasa) + H₂O₂ + ClO⁻ → HOCl + H₂O

 ¿ClO⁻ (desde ClO₂) puede ser sustrato de MPO?
 → POSIBLE pero NO DEMOSTRADO experimentalmente

SELECTIVIDAD:
- ESPACIAL (fagolisosoma vs citoplasma): Factor >100×
- FUNCIONAL (solo targets fagocitados afectados)

LIMITACIONES:
✗ Solo afecta virus LIBRE o células infectadas apoptóticas
✗ Virus intracelular (no fagocitado) NO afectado
✗ Requiere sistema inmune funcional
✗ En COVID severo: Neutrofilia patológica → Riesgo de daño tisular
```

### Escenario D: Daño Diferencial (Reparación)

```
CAPACIDAD DE REPARACIÓN: VIRUS vs CÉLULA
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

VIRUS (Sin reparación) CÉLULA (Con reparación)
┌─────────────────────────┐ ┌─────────────────────────┐
│ │ │ │
│ Spike protein │ │ Proteoma (500k prot) │
│ - 40 Cys (20 puentes) │ │ - 1M tioles totales │
│ │ │ │
│ Oxidación 1-2 puentes │ │ Oxidación 10% │
│ -> │ │ -> │
│ RBD desnaturalizado │ │ REPARACIÓN: │
│ -> │ │ ┌─────────────┐ │
│ No unión a ACE2 │ │ │Tioredoxina │ │
│ -> │ │ │Proteasoma │ │
│ INACTIVACIÓN VIRAL ✗ │ │ │Síntesis nova│ │
│ (IRREVERSIBLE) │ │ └─────────────┘ │
│ │ │ -> │
│ Sin metabolismo │ │ Función restaurada │
│ Sin enzimas reparación │ │ CÉLULA VIABLE ✓ │
│ │ │ │
└─────────────────────────┘ └─────────────────────────┘

VENTANA TEÓRICA:
- Dosis que oxida 1% de tioles:
 * Virus: 99% inactivación (crítico pocos targets)
 * Célula: 2% daño (redundancia, reparación)

FACTOR: 50× (99% / 2%)

PROBLEMA CRÍTICO:
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Si virus está INTRACELULAR (célula infectada):

┌────────────────────────────────────────────┐
│ CÉLULA INFECTADA │
│ │
│ [ClO₂] = 100 μM (uniforme intracelular) │
│ -> -> │
│ Tioles virales Tioles celulares │
│ (11,200) (1,000,000) │
│ -> -> │
│ P(oxidar) = 1.1% P(oxidar) = 98.9% │
│ │
│ VIRUS RECIBE MENOS DAÑO QUE CÉLULA │
│ (Por abundancia relativa) │
└────────────────────────────────────────────┘

CONTRADICCIÓN:
- Ventana terapéutica solo existe si virus es EXTRACELULAR
- En COVID-19: Virus es mayormente INTRACELULAR
- CONCLUSIÓN: Escenario D es IMPLAUSIBLE para virus intracelular
```

### Escenario E: Selectividad Inmune Indirecta

```
MARCAJE INMUNE DE CÉLULAS INFECTADAS
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

FASE 1: Oxidación diferencial
──────────────────────────────
Célula infectada (GSH bajo) recibe 2-3× más daño que sana

FASE 2: Señales de estrés
─────────────────────────

┌─────────────────────────────────────────┐
│ CÉLULA INFECTADA (oxidada) │
│ │
│ ┌──────────────────────────────────┐ │
│ │ MEMBRANA: │ │
│ │ - Fosfatidilserina externa ✓ │ │
│ │ - MICA/MICB expresión <- │ │
│ │ - Calreticulina externa ✓ │ │
│ └──────────────────────────────────┘ │
│ │
│ LIBERACIÓN: │
│ - ATP extracelular │
│ - HMGB1 (DAMP) │
│ - Citoquinas de estrés │
│ │
│ SEÑAL: "CÓMEME" / "ELIMÍNAME" │
│ │
└─────────────────────────────────────────┘
 ->
 ┌────────────────┐
 │ MACRÓFAGO │
 │ ┌──────────┐ │
 │ │Fagocitosis│ │
 │ └──────────┘ │
 │ -> │
 │ Destrucción │
 │ de célula │
 │ infectada │
 └────────────────┘

FASE 3: Clearance selectivo
────────────────────────────
- Células sanas (GSH alto): Sin marcaje → Superviven
- Células infectadas (GSH bajo + ClO₂): Marcaje → Eliminadas

SELECTIVIDAD: Variable (dependiente de respuesta inmune)

MECANISMO:
- NO es antiviral DIRECTO
- ES inmunomodulador
- ClO₂ actúa como "adjuvante" para clearance inmune

VENTAJAS:
✓ Aprovecha sistema inmune natural
✓ Selectividad conferida por inmunidad, no por química

DESVENTAJAS:
✗ Requiere sistema inmune funcional
✗ En COVID severo (tormenta citoquinas): Podría EMPEORAR
✗ Efecto es INDIRECTO → Difícil de predecir
✗ Variabilidad inter-paciente ALTA
```

---

## PATHWAY INTEGRADO MULTI-ETAPA

### Modelo Temporal Completo

```
TIMELINE DE ACCIÓN DE ClO₂ (Si hubiera efecto antiviral)
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

FASE 1: EXTRACELULAR (0-30 minutos)
───────────────────────────────────────────────────────────────
│
│ ALVEOLO / TORRENTE SANGUÍNEO
│ ┌─────────────────────────────────────────────────┐
│ │ │
│ │ [ClO₂] = 10-50 μM (pico tras exposición) │
│ │ │
│ │ ○ ○ ○ ← Viriones libres │
│ │ -> -> -> Oxidación de spike protein │
│ │ ✗ ✗ ✗ Inactivación parcial │
│ │ │
│ │ Eficacia: 10-30% de virus libre inactivado │
│ │ Toxicidad: Baja (exposición corta) │
│ │ │
│ │ CÉLULAS: │
│ │ - - - - - - ClO₂ penetra lentamente │
│ │ | | | | Daño superficial (membrana) │
│ │ - - - - - - Interior aún protegido │
│ │ │
│ └─────────────────────────────────────────────────┘
│
│ CONTRIBUCIÓN A EFICACIA TOTAL: 10-30%
│
▼

FASE 2: PENETRACIÓN CELULAR (30 min - 6 horas)
───────────────────────────────────────────────────────────────
│
│ INTRACELULAR
│ ┌─────────────────────────────────────────────────┐
│ │ │
│ │ ClO₂ equilibrado intra/extracelular │
│ │ │
│ │ CÉLULA SANA: CÉLULA INFECTADA: │
│ │ - - - - - - - - - - - - - - - - - - - - - - │
│ │ | GSH: 5 mM | | GSH: 1.5mM | │
│ │ | | | ○ ← Virus | │
│ │ | Daño: 2% | | | │
│ │ | | | Daño: 6% | │
│ │ | VIABLE ✓ | | | │
│ │ - - - - - - - - - - - | APOPTOSIS | │
│ │ | -> | │
│ │ | PS → ext | ← Marcaje
│ │ | DAMPs <- | │
│ │ - - - - - - - - - - - │
│ │ │
│ │ Células infectadas → Apoptosis/Marcaje │
│ │ Prevención de propagación viral │
│ │ │
│ └─────────────────────────────────────────────────┘
│
│ CONTRIBUCIÓN A EFICACIA TOTAL: 20-40%
│
▼

FASE 3: RESPUESTA INMUNE (6-24 horas)
───────────────────────────────────────────────────────────────
│
│ CLEARANCE INMUNE
│ ┌─────────────────────────────────────────────────┐
│ │ │
│ │ NEUTRÓFILOS / MACRÓFAGOS │
│ │ │
│ │ ┌─────────────┐ │
│ │ │ FAGOCITOSIS │ │
│ │ │ de: │ │
│ │ │ - Virus ○ │ │
│ │ │ - Células ✗ │ ← Apoptóticas/Marcadas │
│ │ └──────┬──────┘ │
│ │ -> │
│ │ ┌──────────────┐ │
│ │ │FAGOLISOSOMA │ │
│ │ │ │ │
│ │ │ MPO + H₂O₂ │ │
│ │ │ + ClO⁻ │ ← Desde ClO₂? │
│ │ │ -> │ │
│ │ │ HOCl (mM) │ ← Concentración letal │
│ │ │ -> │ │
│ │ │ Destrucción │ │
│ │ └──────────────┘ │
│ │ │
│ │ Eliminación selectiva de: │
│ │ - Virus libre fagocitado │
│ │ - Células infectadas apoptóticas │
│ │ │
│ └─────────────────────────────────────────────────┘
│
│ CONTRIBUCIÓN A EFICACIA TOTAL: 30-50%
│
▼

RESULTADO FINAL (24-48 horas)
───────────────────────────────────────────────────────────────

 EFICACIA TOTAL ESTIMADA: 30-70% (sumatoria de fases)

 Comparación con antivirales estándar:
 - Remdesivir: 70-80%
 - Paxlovid: >85%
 - ClO₂ (estimado): 30-70% (altamente variable)

 TOXICIDAD: Moderada (metHb, daño celular, inflamación)

 RATIO BENEFICIO/RIESGO: DESFAVORABLE (sin evidencia clínica)

 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
```

---

## ÁRBOL DE DECISIÓN: INVESTIGACIÓN

```
DECISIÓN: ¿INVESTIGAR ClO₂ COMO ANTIVIRAL?
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

 INICIO
 │
 ->
 ┌───────────────────────┐
 │ ESTUDIOS IN VITRO │
 │ ───────────────── │
 │ - SI experimental │
 │ - Mecanismo │
 │ - Rol de GSH │
 │ - ROS secundarios │
 └──────────┬────────────┘
 │
 ┌────────────┴─────────────┐
 │ │
 -> ->
 SI > 10 ? SI < 10 ?
 (Selectivo) (No selectivo)
 │ │
 -> ->
 ┌───────────────┐ ┌──────────────┐
 │ PROCEDER A │ │ DETENER │
 │ PRECLÍNICOS │ │ INVESTIGACIÓN│
 └───────┬───────┘ └──────────────┘
 │ │
 -> ->
 ┌──────────────────┐ CONCLUSIÓN:
 │ ANIMAL MODEL │ "ClO₂ NO es
 │ ───────────── │ selectivo.
 │ - Farmacocin. │ No justifica
 │ - Dosis tóxica │ desarrollo
 │ - Eficacia │ clínico."
 │ - Histopatología│
 └────────┬─────────┘
 │
 ┌──────┴───────┐
 │ │
 -> ->
Margen > 10× ? Margen < 10× ?
(Seguro) (Tóxico)
 │ │
 -> ->
┌──────────┐ ┌─────────────┐
│FASE I │ │ DETENER │
│(Seguridad)│ │ DESARROLLO│
└────┬─────┘ └─────────────┘
 │ │
 -> ->
¿Seguro? CONCLUSIÓN:
 │ "Toxicidad
 SI│ inaceptable.
 -> No proceder
┌──────────┐ a humanos."
│FASE II │
│(Eficacia)│
└────┬─────┘
 │
 ->
¿Eficacia > 50% reducción viral?
 │
 SI│
 ->
┌──────────┐
│FASE III │
│(Confirma)│
└────┬─────┘
 │
 ->
¿Confirmación?
 │
 SI│
 ->
┌─────────────────┐
│ APROBACIÓN │
│ (Condicional) │
└─────────────────┘

ESTADO ACTUAL DE ClO₂:
 - - - - - - - - - - - - - - - - - - - - - - -
❌ Faltan estudios in vitro rigurosos (SI experimental)
❌ Faltan estudios preclínicos (farmacocinética, margen)
❌ Faltan ensayos clínicos controlados (Fase I, II, III)

CONCLUSIÓN: NO ha pasado ni el primer paso del árbol.
 Uso clínico actual NO está justificado.
```

---

## COMPARACIÓN CON ANTIVIRALES

### Gráfico: Selectivity Index (SI)

```
ÍNDICE DE SELECTIVIDAD (SI)
Escala logarítmica
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

SI
1000 ─┤ ██████████ Paxlovid
 │ ██████████ (>1000)
 │
 │
 100 ─┤ ████████ Remdesivir
 │ ████████ (~100)
 │
 │
 10 ─┤ ██████ Margen MÍNIMO aceptable
 │ ██████ para terapéutica
 │ ████
 │ ████ ClO₂ (estimado, 5-30)
 1 ─┼──████────────────────────────────────────────────────
 │
 │ ZONA DE TOXICIDAD
 │ (SI < 10 → Tóxico o marginalmente selectivo)
 │
 0 ─┴───────────────────────────────────────────────────

INTERPRETACIÓN:
 - - - - - - - - - - - - - - -

SI < 2: Sin selectividad (tóxico)
SI 2-10: Selectividad marginal (riesgoso)
SI 10-100: Selectividad moderada (candidato)
SI >100: Alta selectividad (buen fármaco)

ClO₂ (5-30): MARGINAL-RIESGOSO
 Comparable a quimioterapias (Bleomicina SI~2-5)
 NO comparable a antivirales (Remdesivir SI>100)
```

### Tabla Comparativa Multidimensional

```
COMPARACIÓN: ClO₂ vs ANTIVIRALES APROBADOS
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Criterio │ ClO₂ │Remdesivir│ Paxlovid │Molnupiravir
──────────────────┼─────────┼──────────┼──────────┼────────────
QUÍMICA │ │ │ │
──────────────────┼─────────┼──────────┼──────────┼────────────
Mecanismo │Oxidación│Inh. Pol │Inh. Prot │Mutagénesis
Target │Inespecí.│RdRp viral│3CLpro vir│RdRp viral
Selectividad │Ninguna │Alta │Muy Alta │Alta
──────────────────┼─────────┼──────────┼──────────┼────────────
EFICACIA │ │ │ │
──────────────────┼─────────┼──────────┼──────────┼────────────
SI experimental │5-30* │>100 │>1000 │>50
Reducción viral │30-70%* │70-80% │>85% │50-70%
Evidencia clínica │Escasa │Sólida │Sólida │Moderada
Aprobación FDA │NO │SÍ (EUA) │SÍ │SÍ (EUA)
──────────────────┼─────────┼──────────┼──────────┼────────────
SEGURIDAD │ │ │ │
──────────────────┼─────────┼──────────┼──────────┼────────────
Toxicidad │Moderada │Baja-Mod │Baja │Moderada
Efectos adversos │MetHb │Hepático │Mínimos │Mutagénesis?
Margen terapéut. │Estrecho │Amplio │Muy Amplio│Amplio
──────────────────┼─────────┼──────────┼──────────┼────────────
PRÁCTICA │ │ │ │
──────────────────┼─────────┼──────────┼──────────┼────────────
Vía admin. │Oral? │IV │Oral │Oral
Costo │Bajo │Alto │Alto │Moderado
Disponibilidad │Alta** │Limitada │Moderada │Moderada
Recomendación │NO*** │SÍ (hosp.)│SÍ (amb.) │SÍ (amb.)
──────────────────┼─────────┼──────────┼──────────┼────────────

* Estimado teórico, sin validación experimental rigurosa
** Disponible como desinfectante, NO aprobado como antiviral
*** NO recomendado por agencias sanitarias (FDA, EMA, OMS)

CONCLUSIÓN:
ClO₂ es INFERIOR en todos los parámetros críticos vs antivirales.
Uso clínico NO justificado sin evidencia experimental sólida.
```

---

## CONCLUSIONES VISUALES

### Mapa Conceptual: ¿Por qué ClO₂ NO es selectivo?

```
 ┌─────────────────────────────┐
 │ ClO₂ COMO ANTIVIRAL │
 │ ¿Puede ser selectivo? │
 └──────────────┬──────────────┘
 │
 ┌─────────────────┴─────────────────┐
 │ │
 -> ->
 ┌────────────────────┐ ┌────────────────────┐
 │ NIVEL MOLECULAR │ │ NIVEL SISTÉMICO │
 │ (Química directa) │ │ (Biología indirecta)│
 └─────────┬──────────┘ └─────────┬──────────┘
 │ │
 ┌───────┴────────┐ ┌──────────┴──────────┐
 │ │ │ │
 -> -> -> ->
 ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────┐
 │Termodin. │ │Cinética │ │Espacial │ │Estado Redox │
 │ │ │ │ │ │ │ │
 │ΔG viral │ │k_virus ≈ │ │Virus ext.│ │Célula infe. │
 │ ≈ │ │k_humano │ │vs célula │ │GSH bajo │
 │ΔG humano │ │ │ │ │ │ │
 │ │ │NO │ │Ventana │ │Factor 2-3× │
 │NO │ │selectivo │ │<5 min │ │INSUFICIENTE │
 │selectivo │ │ │ │ │ │ │
 └──────────┘ └──────────┘ │Factor │ └──────────────┘
 │1.5-2× │
 │INSUFI. │ ┌──────────────┐
 └──────────┘ │ROS secundarios│
 │(HOCl vía MPO)│
 ┌───────────────┐ │ │
 │Abundancia │ │Requiere │
 │ │ │fagocitosis │
 │Humano:Viral │ │ │
 │= 1,000,000: │ │COMPLEMENTARIO│
 │ 11,200 │ │ │
 │ │ └──────────────┘
 │= 89:1 │
 │ │ ┌──────────────┐
 │Estadística │ │Selectividad │
 │favorece │ │inmune │
 │HUMANO │ │(marcaje) │
 └───────────────┘ │ │
 │Indirecta, │
 │variable │
 │ │
 │INCIERTA │
 └──────────────┘
 │
 ->
 ┌─────────────────────────────┐
 │ CONCLUSIÓN INTEGRADA │
 │ │
 │ Selectividad molecular: NO │
 │ │
 │ Selectividad sistémica: │
 │ POSIBLE pero DÉBIL (5-30×) │
 │ │
 │ Insuficiente para uso │
 │ terapéutico seguro │
 │ │
 │ Evidencia experimental: │
 │ REQUERIDA │
 └─────────────────────────────┘
```

---

**DOCUMENTO:** Diagramas y Modelos Visuales
**VERSIÓN:** 1.0
**FECHA:** 2025-12-26
**PROPÓSITO:** Complemento visual al análisis técnico de selectividad
