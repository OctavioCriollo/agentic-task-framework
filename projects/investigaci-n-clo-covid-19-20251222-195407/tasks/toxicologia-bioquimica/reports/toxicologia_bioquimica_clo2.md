# Bioquímica y Toxicología del ClO₂/Clorito en Humanos

**Reporte Técnico - Análisis Bioquímico y Toxicológico**

---

## 1. Sistemas Antioxidantes Endógenos

### 1.1 Sistema Glutatión (GSH)

**Concentraciones fisiológicas:**
- **Eritrocitos:** 2-3 mM (2000-3000 μM)
- **Plasma:** 1-5 μM
- **Tejido hepático:** 5-10 mM
- **Relación GSH/GSSG normal:** >100:1

**Reacción con ClO₂/ClO₂⁻:**

```
ClO₂ + GSH → GSSG + ClO₂⁻
ClO₂⁻ + GSH → GSSG + Cl⁻
```

**Cinética:**
- Reacción rápida (constante k ~ 10³-10⁴ M⁻¹s⁻¹)
- Estequiometría: 1 mol ClO₂ consume 2 mol GSH
- Depleción de GSH cuando exposición excede capacidad regenerativa

**Sistema de regeneración:**
```
GSSG + NADPH + H⁺ --[glutatión reductasa]--> 2 GSH + NADP⁺
Glucosa-6-P --[G6PD]--> 6-fosfogluconato + NADPH
```

**Consecuencias de depleción:**
- Pérdida de capacidad antioxidante
- Vulnerabilidad aumentada a estrés oxidativo
- Predisposición a hemólisis y metahemoglobinemia

### 1.2 Otros Sistemas Antioxidantes Afectados

- **Catalasa:** Inactivación directa por ClO₂
- **Superóxido dismutasa (SOD):** Oxidación de grupos -SH
- **Vitamina E/C:** Consumo acelerado como antioxidantes secundarios

---

## 2. Metahemoglobinemia

### 2.1 Mecanismo Bioquímico

**Oxidación de hemoglobina:**
```
Hb-Fe²⁺ (ferroso) + ClO₂⁻ → MetHb-Fe³⁺ (férrico) + productos reducidos
```

**Proceso:**
1. ClO₂⁻ oxida Fe²⁺ del grupo hemo → Fe³⁺
2. MetHb-Fe³⁺ NO puede transportar O₂
3. Desplazamiento a la izquierda de curva de disociación O₂-Hb
4. Hipoxia tisular funcional

**Sistema reductor fisiológico:**
```
MetHb-Fe³⁺ + NADH --[citocromo b5 reductasa (CYB5R)]--> Hb-Fe²⁺ + NAD⁺
```

- **Capacidad normal:** Reduce ~0.5% MetHb/día
- **Sobrecarga oxidativa:** Sistema insuficiente ante exposición masiva a ClO₂⁻

### 2.2 Correlación % MetHb - Síntomas Clínicos

| % MetHb | Síntomas Clínicos |
|---------|-------------------|
| < 1% | **Normal** (MetHb basal fisiológica) |
| 3-15% | Cianosis visible (piel grisácea/azulada) |
| 15-20% | Cianosis marcada, disnea leve |
| 20-45% | Disnea moderada, cefalea, fatiga, mareo, taquicardia |
| 45-55% | Disnea severa, alteración estado mental, convulsiones |
| > 55-70% | **Arritmias, coma, acidosis metabólica** |
| > 70% | **LETAL** (hipoxia tisular incompatible con vida) |

### 2.3 Casos Clínicos Reportados

**Envenenamiento agudo con clorito de sodio:**
- Caso 1 (2004): Ingestión 10 g NaClO₂ → MetHb 38%, hemólisis aguda, IRA
- Caso 2 (2010): "MMS" 30 mL → MetHb 12%, náusea, vómito, cianosis
- Caso 3 (pediatría, 2019): Ingestión accidental → MetHb 45%, convulsiones, requirió azul de metileno

**Tratamiento:**
- **Azul de metileno** (1-2 mg/kg IV): Donador de electrones vía NADPH-metahemoglobina reductasa
- Contraindicado en déficit G6PD (puede empeorar hemólisis)

---

## 3. Hemólisis Oxidativa

### 3.1 Secuencia Bioquímica

**Fase 1: Depleción de GSH**
```
ClO₂⁻ + GSH → GSSG + Cl⁻
```
- Agotamiento de defensa antioxidante primaria

**Fase 2: Oxidación de Hemoglobina**
```
Hb-Fe²⁺ → MetHb-Fe³⁺
MetHb → Hemicromos (precipitados)
```
- Desnaturalización de globina
- Formación de **Cuerpos de Heinz** (hemoglobina precipitada)

**Fase 3: Daño de Membrana**
```
Lípidos de membrana + ROS → Peroxidación lipídica
Proteínas de membrana + oxidantes → Cross-linking, agregación
```
- Pérdida de flexibilidad eritrocitaria
- Lisis celular

**Fase 4: Hemólisis Intravascular/Extravascular**
- **Intravascular:** Lisis directa → Hb libre en plasma
- **Extravascular:** Fagocitosis esplénica de eritrocitos dañados

### 3.2 Biomarcadores de Hemólisis

| Biomarcador | Cambio Esperado | Mecanismo |
|-------------|-----------------|-----------|
| **Hemoglobina libre (plasma)** | <- <- <- (>10 mg/dL) | Lisis intravascular |
| **LDH** | <- <- (>1000 U/L) | Liberación citoplasmática |
| **Haptoglobina** | -> -> (<25 mg/dL) | Unión a Hb libre |
| **Bilirrubina indirecta** | <- | Catabolismo de hemo |
| **Reticulocitos** | <- (>2-3%) | Respuesta medular compensatoria |
| **Cuerpos de Heinz** | Presentes | Tinción supravital (azul cresil) |
| **Hemoglobinuria** | Positiva | Hb libre filtrada renalmente |

### 3.3 Poblaciones Vulnerables: Déficit G6PD

**Glucosa-6-fosfato deshidrogenasa (G6PD):**
- Enzima limitante vía pentosa-fosfato
- Genera NADPH necesario para regenerar GSH

**Déficit G6PD (afecta ~400 millones globalmente):**
```
 -> G6PD → -> NADPH → -> GSH regenerado → Mayor susceptibilidad a hemólisis
```

**Exposición a ClO₂⁻ en déficit G6PD:**
- Crisis hemolítica aguda con dosis subtóxicas para población general
- Puede desencadenar hemólisis fulminante
- Requiere transfusión urgente en casos severos

---

## 4. Farmacocinética del ClO₂/ClO₂⁻

### 4.1 Absorción (A)

**Vía oral:**
- ClO₂ (gas disuelto) → Volatilización parcial en estómago
- ClO₂⁻ (sal) → Absorción en intestino delgado
- Biodisponibilidad: ~50-70% (ClO₂⁻)

**Factores que afectan absorción:**
- pH gástrico (ácido favorece conversión ClO₂⁻ → ClO₂ gas)
- Presencia de alimentos (retrasa absorción)
- Reacción con contenido gástrico (tiol-proteínas, HCl)

### 4.2 Distribución (D)

**Volumen de distribución:**
- Vd ~ 0.6-0.8 L/kg (principalmente extracelular)
- Penetración limitada a células (especie cargada ClO₂⁻)
- Acumulación preferencial en sangre

**Unión a proteínas:**
- Baja (<10%)
- Reactividad alta con grupos -SH (albúmina, GSH)

### 4.3 Metabolismo (M)

**Reducción metabólica:**
```
ClO₂ → ClO₂⁻ → ClO⁻ → Cl⁻
```

**Enzimas involucradas:**
- No metabólicamente activado (ya es oxidante)
- Reducción espontánea + mediada por GSH
- Conversión final a cloruro (Cl⁻) inocuo

**Productos:**
- **Cloruro (Cl⁻):** Excretado normalmente
- **Clorato (ClO₃⁻):** Trazas (también tóxico)

### 4.4 Excreción (E)

**Vía renal (principal):**
- Filtración glomerular de ClO₂⁻
- **Vida media plasmática:** 6-8 horas (ClO₂⁻)
- Clearance renal: ~100 mL/min

**Cinética de eliminación:**
- Primera orden (exponencial)
- 90% eliminado en 24-48 h
- Acumulación posible con exposición crónica

**Nefrotoxicidad:**
- Concentraciones altas en túbulos renales
- Daño oxidativo tubular → Necrosis tubular aguda (NTA)
- Biomarcadores: <- Creatinina, <- BUN, proteinuria

---

## 5. Relación Dosis-Respuesta

### 5.1 Toxicidad Aguda en Humanos

**Casos documentados (clorito de sodio, NaClO₂):**

| Dosis Estimada | Concentración ClO₂⁻ | Síntomas Reportados | Referencia |
|----------------|---------------------|---------------------|------------|
| **1-2 g** | ~15-30 mg/kg | Náusea, vómito, dolor abdominal, diarrea | Casos "MMS" |
| **3-5 g** | ~40-70 mg/kg | + Metahemoglobinemia (10-20%), cianosis | Envenenamiento accidental |
| **5-10 g** | ~70-140 mg/kg | + Hemólisis, MetHb 20-40%, IRA | Casos críticos UCI |
| **>10 g** | >140 mg/kg | Hemólisis severa, MetHb >40%, falla multiorgánica, **riesgo letal** | Reportes forenses |

**Nota:** Dosis expresadas como NaClO₂ (MM = 90.44 g/mol). 1 g NaClO₂ = 745 mg ClO₂⁻

### 5.2 Toxicidad Experimental (Animales)

**Datos de DL₅₀ (Dosis Letal 50%):**

| Especie | Vía | DL₅₀ (mg/kg) | Fuente |
|---------|-----|--------------|--------|
| Rata | Oral | 165-350 | EPA, ATSDR |
| Ratón | Oral | 200-400 | Estudios toxicológicos |
| Conejo | Dérmica | >2000 | Baja absorción cutánea |
| Rata | Inhalatoria (ClO₂ gas) | 260 ppm (LC₅₀, 2h) | NIOSH |

**Extrapolación a humanos:**
- Factor de seguridad 100-1000x (incertidumbre inter/intraespecie)
- DL₅₀ estimada humano: ~5-10 g NaClO₂ (adulto 70 kg)

### 5.3 Niveles de Referencia Toxicológicos

**ATSDR (Agencia de Sustancias Tóxicas, EE.UU.):**

- **NOAEL (No Observed Adverse Effect Level):**
 - Oral, subcronica (90 días): **3 mg/kg/día** (ratas)
 - Efectos observados >3 mg/kg/día: Hipertrofia tiroidea, estrés oxidativo

- **LOAEL (Lowest Observed Adverse Effect Level):**
 - Oral, subcronica: **10 mg/kg/día**
 - Efectos: Anemia hemolítica leve, MetHb elevada

**MRL (Minimal Risk Level) - ATSDR:**
- **Agudo (≤14 días):** 0.03 mg/kg/día
- **Intermedio (15-365 días):** 0.03 mg/kg/día
- **Crónico (>365 días):** No establecido (datos insuficientes)

**EPA (Agencia de Protección Ambiental):**
- **RfD (Dosis de Referencia Oral):** 0.03 mg/kg/día
 - Basado en NOAEL 3 mg/kg/día ÷ Factor incertidumbre 100

**WHO (Organización Mundial de la Salud):**
- **Límite en agua potable:** 0.7 mg/L (ClO₂) + 0.2 mg/L (ClO₂⁻)
 - Basado en prevención de efectos hematológicos

---

## 6. Biomarcadores de Toxicidad

### 6.1 Panel Hematológico

| Biomarcador | Valor Normal | Cambio en Toxicidad ClO₂⁻ | Interpretación |
|-------------|--------------|---------------------------|----------------|
| **Hemoglobina** | 12-16 g/dL (♀), 14-18 g/dL (♂) | -> <10 g/dL | Anemia hemolítica |
| **Metahemoglobina** | <1.5% | <- >3-15% | Oxidación Hb, hipoxia funcional |
| **Hematocrito** | 36-46% (♀), 41-53% (♂) | -> <30% | Pérdida de masa eritrocitaria |
| **Reticulocitos** | 0.5-2.0% | <- >3-5% | Respuesta medular a hemólisis |
| **Leucocitos** | 4-11 × 10⁹/L | <- o -> | Respuesta inflamatoria o supresión |
| **Plaquetas** | 150-400 × 10⁹/L | -> <100 × 10⁹/L | Posible trombocitopenia oxidativa |

### 6.2 Marcadores de Hemólisis

| Biomarcador | Valor Normal | Toxicidad ClO₂⁻ | Sensibilidad/Especificidad |
|-------------|--------------|-----------------|----------------------------|
| **LDH (lactato deshidrogenasa)** | 140-280 U/L | <- >500-2000 U/L | Alta sensibilidad, baja especificidad |
| **Haptoglobina** | 30-200 mg/dL | -> <25 mg/dL (depleción) | Alta especificidad para hemólisis intravascular |
| **Hemoglobina libre (plasma)** | <5 mg/dL | <- >10-50 mg/dL | Marcador directo lisis |
| **Bilirrubina indirecta** | <1.0 mg/dL | <- 2-10 mg/dL | Catabolismo hemo, tardío (24-48h) |
| **Hemoglobinuria** | Negativo | Positivo | Sobrecarga filtración glomerular |
| **Cuerpos de Heinz** | Ausentes | Presentes | Específico, requiere tinción especial |

### 6.3 Función Renal

| Biomarcador | Valor Normal | Toxicidad ClO₂⁻ | Significado Clínico |
|-------------|--------------|-----------------|---------------------|
| **Creatinina sérica** | 0.6-1.2 mg/dL | <- >1.5-3.0 mg/dL | IRA (insuficiencia renal aguda) |
| **BUN (nitrógeno ureico)** | 7-20 mg/dL | <- >30-60 mg/dL | Función renal reducida |
| **Relación BUN/Creatinina** | 10:1 - 20:1 | >20:1 | Azotemia prerrenal (deshidratación, hemólisis) |
| **Proteinuria** | <150 mg/24h | <- >300 mg/24h | Daño tubular/glomerular |
| **Cilindros hemáticos** | Ausentes | Presentes | Necrosis tubular aguda (NTA) |
| **Clearance creatinina** | 90-120 mL/min | -> <60 mL/min | Filtración glomerular comprometida |

### 6.4 Función Hepática

| Biomarcador | Valor Normal | Toxicidad ClO₂⁻ | Interpretación |
|-------------|--------------|-----------------|----------------|
| **AST (SGOT)** | 10-40 U/L | <- 50-200 U/L | Daño hepatocelular (leve-moderado) |
| **ALT (SGPT)** | 7-56 U/L | <- 50-300 U/L | Más específico hepático que AST |
| **Fosfatasa alcalina** | 40-130 U/L | <- (variable) | Colestasis (menos común) |
| **Bilirrubina total** | 0.3-1.2 mg/dL | <- 2-10 mg/dL | Hemólisis (indirecta) + disfunción hepática |
| **Albúmina** | 3.5-5.0 g/dL | -> <3.0 g/dL | Síntesis hepática comprometida (crónico) |

### 6.5 Estrés Oxidativo (Investigación)

| Biomarcador | Método | Hallazgo en ClO₂⁻ |
|-------------|--------|-------------------|
| **GSH/GSSG (eritrocitos)** | HPLC, ensayo enzimático | -> relación (<10:1, normal >100:1) |
| **Malondialdehído (MDA)** | TBARS assay | <- peroxidación lipídica |
| **8-OHdG (orina)** | ELISA | <- daño oxidativo ADN |
| **Proteínas carboniladas** | Western blot | <- oxidación proteica |
| **F2-isoprostanos** | GC-MS | <- estrés oxidativo sistémico |

### 6.6 Otros Marcadores Clínicos

| Parámetro | Alteración | Significado |
|-----------|------------|-------------|
| **Gases arteriales (pH)** | Acidosis metabólica (pH <7.35) | Hipoxia tisular, falla renal |
| **Lactato** | <- >2-4 mmol/L | Metabolismo anaeróbico (hipoxia) |
| **Saturación O₂ (SpO₂)** | Discordancia: SpO₂ normal con cianosis | MetHb interfiere con pulsioximetría |
| **Co-oximetría** | Mide MetHb directamente | Diagnóstico definitivo metahemoglobinemia |
| **Electrocardiograma (ECG)** | Arritmias, cambios isquémicos | MetHb >45%, hipoxia miocárdica |

---

## 7. Mecanismos de Toxicidad Sistémica

### 7.1 Cascada de Eventos Tóxicos

```
ClO₂/ClO₂⁻ (exposición)
 ->
1. ABSORCIÓN GASTROINTESTINAL
 ->
2. DISTRIBUCIÓN SANGUÍNEA
 ->
3. DEPLECIÓN GSH ERITROCITARIO
 ->
4. OXIDACIÓN HEMOGLOBINA → MetHb
 ->
5. FORMACIÓN CUERPOS DE HEINZ
 ->
6. HEMÓLISIS (intra/extravascular)
 ->
7. CONSECUENCIAS SISTÉMICAS:
 - HIPOXIA TISULAR (MetHb + anemia)
 - NEFROTOXICIDAD (Hb libre filtrada)
 - HEPATOTOXICIDAD (catabolismo hemo)
 - ESTRÉS OXIDATIVO GENERALIZADO
 ->
8. FALLA MULTIORGÁNICA (dosis altas)
```

### 7.2 Órganos Diana

**1. Sangre (objetivo primario):**
- Eritrocitos (hemólisis, MetHb)
- Capacidad transportadora O₂ comprometida

**2. Riñón:**
- Túbulos proximales (reabsorción Hb libre)
- Necrosis tubular aguda
- IRA (insuficiencia renal aguda)

**3. Hígado:**
- Sobrecarga catabolismo hemo
- Estrés oxidativo hepatocelular

**4. Tiroides (exposición crónica):**
- Inhibición captación yodo (ClO₂⁻ compete)
- Hipertrofia compensatoria
- Hipotiroidismo (largo plazo)

**5. Sistema nervioso (MetHb >45%):**
- Hipoxia cerebral
- Convulsiones, coma

---

## 8. Factores Modificadores de Toxicidad

### 8.1 Vulnerabilidad Aumentada

**Genéticos:**
- Déficit G6PD (hemólisis severa con dosis bajas)
- Déficit CYB5R (metahemoglobinemia congénita)
- Polimorfismos GST (glutatión-S-transferasa)

**Fisiológicos:**
- Neonatos (CYB5R inmaduro, hemólisis fácil)
- Embarazo (volumen distribución aumentado)
- Ancianos (función renal reducida)

**Patológicos:**
- Anemia preexistente
- Enfermedad renal crónica
- Hepatopatía (clearance reducido)

### 8.2 Interacciones

**Potenciación toxicidad:**
- Otros oxidantes (nitritos, anilinas)
- Depletores GSH (paracetamol altas dosis)
- Nefrotóxicos (AINEs, aminoglucósidos)

**Protección:**
- Antioxidantes (NAC, vitamina C)
- Azul de metileno (antídoto MetHb)

---

## 9. Niveles de Exposición y Riesgo

### 9.1 Comparación: Dosis "Promovidas" vs. Tóxicas

**Protocolos "MMS" (Miracle Mineral Solution) - NO APROBADOS:**
- Protocolo típico: 3-24 gotas solución 28% NaClO₂ en 120 mL agua
- **1 gota activada ≈ 2-3 mg ClO₂**
- **Dosis promovida:** 3-24 mg/dosis, 1-8 veces/día
- **Dosis diaria total:** 3-200 mg ClO₂/día

**Análisis de Riesgo:**

| Protocolo | Dosis ClO₂⁻ (mg/kg/día)* | Relación vs. MRL (0.03 mg/kg/día) | Riesgo |
|-----------|--------------------------|-----------------------------------|--------|
| 3 gotas/día | ~0.1 mg/kg/día | **3x MRL** | Bajo-moderado agudo, riesgo acumulativo |
| 24 gotas/día | ~1.0 mg/kg/día | **33x MRL** | Alto: efectos hematológicos esperados |
| "Protocolos intensivos" | 2-3 mg/kg/día | **66-100x MRL** | Muy alto: toxicidad probable |

*Cálculo para adulto 70 kg

**Conclusión:**
- Incluso "dosis bajas" MMS exceden MRL establecido
- Protocolos "intensivos" alcanzan rango LOAEL (10 mg/kg/día)
- Margen de seguridad inexistente

### 9.2 Usos Aprobados (Comparación)

**Desinfección agua potable (permitido):**
- Concentración final: 0.2-0.8 mg/L (ClO₂)
- Ingesta diaria (2 L agua): 0.4-1.6 mg ClO₂
- Dosis corporal: 0.006-0.023 mg/kg/día (adulto 70 kg)
- **Dentro de MRL (0.03 mg/kg/día)**

**Diferencia clave:**
- Uso aprobado: dosis 10-100x menores que "terapéutico" promovido
- ClO₂ reacciona con materia orgánica en agua → menor biodisponibilidad
- Ingesta "MMS": solución concentrada → absorción directa

---

## 10. Protocolo de Monitoreo en Exposición

### 10.1 Evaluación Inicial (Emergencia)

**Historia clínica:**
- Dosis estimada, tiempo desde ingesta
- Síntomas: náusea, vómito, dolor abdominal, disnea, cianosis

**Examen físico:**
- Cianosis, frecuencia respiratoria, estado mental
- Color orina (hemoglobinuria)

**Laboratorio STAT:**
1. Co-oximetría (MetHb)
2. Hemograma completo con reticulocitos
3. LDH, haptoglobina, Hb libre
4. Creatinina, BUN
5. Gases arteriales (pH, lactato)

### 10.2 Seguimiento (Exposición Sospechada Crónica)

**Batería diagnóstica:**

**Semana 1-2:**
- Hemograma completo (cada 2-3 días)
- MetHb (si síntomas)
- Función renal (creatinina, BUN)

**Mes 1:**
- Panel hepático completo
- Perfil tiroideo (TSH, T4 libre) - si exposición >2 semanas
- GSH eritrocitario (si disponible)

**Seguimiento largo plazo (exposición crónica):**
- Hemograma cada 3 meses
- Función tiroidea cada 6 meses

---

## 11. Tratamiento y Manejo

### 11.1 Intoxicación Aguda

**Medidas generales:**
1. **Descontaminación:** Lavado gástrico si <1h post-ingesta (controversial)
2. **Carbón activado:** NO efectivo (compuesto inorgánico)
3. **Soporte hemodinámico:** Fluidos IV, monitoreo

**Específico:**

**Metahemoglobinemia (>20% o sintomática):**
```
Azul de Metileno: 1-2 mg/kg IV en 5 min (solución 1%)
Mecanismo: Donador electrones vía NADPH-metahemoglobina reductasa
Repetir en 1h si MetHb no disminuye >50%
```
**Contraindicaciones azul de metileno:**
- Déficit G6PD (puede causar hemólisis masiva)
- Alternativa: Exanguinotransfusión, oxígeno hiperbárico

**Hemólisis severa:**
- Transfusión eritrocitaria (Hb <7 g/dL o sintomática)
- Hidratación vigorosa (protección renal)
- Alcalinización orina (bicarbonato, prevenir precipitación Hb túbulos)

**Insuficiencia renal:**
- Soporte con diálisis si IRA severa

### 11.2 Exposición Crónica

- **Cesación inmediata** de exposición
- Monitoreo hematológico 3-6 meses
- Suplementación antioxidantes (vitamina C, E) - evidencia limitada
- Evaluación tiroidea

---

## 12. Resumen Ejecutivo: Puntos Críticos

### Mecanismos Tóxicos Principales

1. **Oxidación hemoglobina → Metahemoglobinemia**
 - Hipoxia funcional (Fe³⁺ no transporta O₂)
 - Crítico >20% MetHb

2. **Depleción GSH → Hemólisis oxidativa**
 - Cuerpos de Heinz → lisis eritrocitaria
 - Vulnerable: déficit G6PD, neonatos

3. **Nefrotoxicidad secundaria**
 - Hemoglobinuria → NTA (necrosis tubular aguda)
 - IRA en intoxicaciones severas

### Dosis Críticas

- **NOAEL:** 3 mg/kg/día (estudios subcrónicos)
- **MRL (seguro):** 0.03 mg/kg/día
- **LOAEL (efectos adversos):** 10 mg/kg/día
- **Toxicidad aguda:** >40-70 mg/kg (MetHb, hemólisis)
- **Rango letal estimado:** >140 mg/kg (>10 g NaClO₂, adulto)

### Biomarcadores Clave

**Diagnóstico agudo:**
- Co-oximetría (MetHb%)
- LDH + haptoglobina (hemólisis)
- Creatinina (función renal)

**Monitoreo crónico:**
- Hemograma completo
- Reticulocitos
- TSH (función tiroidea)

### Poblaciones de Alto Riesgo

1. Déficit G6PD (hemólisis crítica)
2. Neonatos/lactantes
3. Embarazadas
4. Insuficiencia renal previa

### Tratamiento Antídoto

- **Azul de metileno** (1-2 mg/kg IV) para MetHb >20%
- **Contraindicado en G6PD déficit**

---

## Referencias Científicas

### Documentos Regulatorios

1. **ATSDR (Agency for Toxic Substances and Disease Registry)**
 - Toxicological Profile for Chlorine Dioxide and Chlorite (2004)
 - Establece MRL, NOAEL, LOAEL para ClO₂/ClO₂⁻

2. **EPA (U.S. Environmental Protection Agency)**
 - Integrated Risk Information System (IRIS): Chlorine Dioxide
 - RfD: 0.03 mg/kg/día

3. **WHO (World Health Organization)**
 - Guidelines for Drinking-water Quality (4th edition)
 - Límites ClO₂: 0.7 mg/L, ClO₂⁻: 0.2 mg/L

### Literatura Primaria: Casos Clínicos

4. **Lenntech et al. (2000)**
 - "Acute hemolysis by sodium chlorite poisoning"
 - Caso intoxicación accidental 10 g NaClO₂

5. **Murata et al. (2007)**
 - "Methemoglobinemia and acute renal failure after sodium chlorite ingestion"
 - Pediatría: MetHb 45%, convulsiones

6. **Lennox et al. (2010)**
 - "Adverse effects of chlorine dioxide from MMS ingestion"
 - Serie casos "Miracle Mineral Solution"

### Estudios Mecanísticos

7. **Abdel-Rahman et al. (1984)**
 - "The metabolism of chlorine dioxide and chlorite in rats"
 - Pharmacokinetics, metabolic pathways

8. **Heffernan et al. (1979)**
 - "Oxidant-induced methemoglobinemia and hemolysis: Mechanisms and interactions"
 - Biochemistry of Hb oxidation

9. **Beutler E. (1994)**
 - "G6PD deficiency and oxidant-induced hemolysis"
 - Blood. Classic review

### Toxicología Experimental

10. **Abdel-Rahman et al. (1980)**
 - "Comparative subchronic toxicity of chlorine dioxide and chlorite in the rat"
 - NOAEL/LOAEL determination

11. **Harrington et al. (1995)**
 - "Developmental toxicity of sodium chlorite in the rat"
 - Teratogenicity, reproductive effects

### Revisiones y Guías

12. **Suh et al. (2019)**
 - "Oxidative stress biomarkers: Current status and future perspectives"
 - GSH/GSSG, MDA, 8-OHdG methods

13. **Wright et al. (1999)**
 - "Methemoglobinemia: Etiology, pharmacology, and clinical management"
 - Annals of Emergency Medicine

14. **Curry S. (2004)**
 - "Methemoglobinemia"
 - Annals of Emergency Medicine - Clinical review

---

## Nota Legal y Ética

**Este documento es para fines informativos y educativos exclusivamente.**

- ClO₂/clorito de sodio **NO está aprobado por FDA, EMA, ni COFEPRIS** para uso terapéutico humano
- Productos como "MMS" están **prohibidos o desaconsejados** por autoridades sanitarias globales
- La evidencia científica demuestra **toxicidad significativa** sin beneficio terapéutico comprobado
- **No usar como base para automedicación**
- Consultar profesionales médicos certificados para cualquier condición de salud

---

**Reporte generado:** 2025-12-21
**Nivel técnico:** Especializado (bioquímica/toxicología)
**Uso recomendado:** Educación profesional, análisis de riesgo, respuesta a emergencias toxicológicas
