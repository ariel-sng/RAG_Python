# Tests - TicketGPT RAG

## 📊 Resumen de Tests Creados

### ✅ Tests Completados (51 tests)

#### 1. **Document Loader** - `tests/utils/test_document_loader.py`
Pruebas para cargar documentos desde archivos.

```
Casos cubiertos:
  ✓ Cargar archivos existentes
  ✓ Manejo de archivos no existentes (FileNotFoundError)
  ✓ Preservación de formato
  ✓ Archivos vacíos
  ✓ Caracteres especiales y acentos
  ✓ Codificación UTF-8

Tests: 7
```

#### 2. **Text Chunker** - `tests/utils/test_text_chunker.py`
Pruebas para dividir texto en chunks con diferentes estrategias.

```
Casos cubiertos:
  ✓ Estrategia "fixed" (tamaño fijo)
  ✓ Estrategia "sentence" (por oraciones)
  ✓ Manejo de overlap (superposición)
  ✓ Validación de tamaño máximo
  ✓ Eliminación de chunks vacíos
  ✓ Estrategia inválida (ValueError)
  ✓ Textos muy cortos y muy largos
  ✓ Múltiples tipos de puntuación
  ✓ Saltos de línea y espacios

Tests: 17
```

#### 3. **Chroma Vector Store** - `tests/repositories/test_chroma_vector_store.py`
Pruebas para almacenamiento de vectores con Chroma.

```
Casos cubiertos:
  ✓ Inicialización con parámetros
  ✓ Guardado de embeddings y metadata
  ✓ Búsqueda por similaridad
  ✓ Respeto del parámetro k
  ✓ Persistencia de datos
  ✓ Colecciones independientes
  ✓ Manejo de metadatos
  ✓ Búsquedas con pocos documentos

Tests: 12
```

#### 4. **Prompt Builder** - `tests/rag/test_prompt_builder.py`
Pruebas para construcción de prompts del LLM.

```
Casos cubiertos:
  ✓ Construcción básica de prompts
  ✓ Inclusión de tags XML (<CONTEXT>, <QUESTION>)
  ✓ Instrucciones del sistema
  ✓ Múltiples chunks de contexto
  ✓ Contexto vacío
  ✓ Caracteres especiales y emojis
  ✓ Preguntas y contextos muy largos
  ✓ Orden de preservación
  ✓ Consistencia de estructura
  ✓ Contenido markdown

Tests: 15
```

---

## 🚀 Ejecutar Tests

### Opción 1: Todos los tests
```bash
pytest
```

### Opción 2: Tests específicos de módulo
```bash
# Document Loader
pytest tests/utils/test_document_loader.py -v

# Text Chunker
pytest tests/utils/test_text_chunker.py -v

# Vector Store
pytest tests/repositories/test_chroma_vector_store.py -v

# Prompt Builder
pytest tests/rag/test_prompt_builder.py -v
```

### Opción 3: Con cobertura
```bash
pytest --cov=src --cov-report=html
# Abre htmlcov/index.html en el navegador
```

### Opción 4: Tests rápidos solamente
```bash
pytest -m "not slow"
```

---

## 📁 Estructura de Carpetas de Tests

```
tests/
├── __init__.py
├── utils/
│   ├── __init__.py
│   ├── test_document_loader.py     (7 tests)
│   └── test_text_chunker.py        (17 tests)
├── repositories/
│   ├── __init__.py
│   └── test_chroma_vector_store.py (12 tests)
└── rag/
    ├── __init__.py
    └── test_prompt_builder.py      (15 tests)
```

---

## 🔧 Dependencias para Tests

Asegúrate de tener instalado:
```bash
pip install pytest pytest-cov
```

---

## 📋 Siguientes Pasos Recomendados

### Prioridad 1: COMPLETADO ✅
- [x] Tests para DocumentLoader
- [x] Tests para TextChunker
- [x] Tests para ChromaVectorStore
- [x] Tests para PromptBuilder

### Prioridad 2: RECOMENDADO
- [ ] Tests para RagIngestionService (con mocks)
  ```bash
  # Crear: tests/rag/test_ingestion_service.py
  ```
- [ ] Tests para RagQueryService (con mocks)
  ```bash
  # Crear: tests/rag/test_query_service.py
  ```

### Prioridad 3: CON MOCKS SOLAMENTE
- [ ] Tests para EmbeddingGenerator (mock OpenAI)
- [ ] Tests para LLMGenerator (mock OpenAI)

**NOTA:** NO crear tests de integración real con OpenAI localmente (muy caro).

---

## 💡 Notas Importantes

1. **Tests Determinísticos:** Los 51 tests actuales son 100% determinísticos (sin dependencias externas costosas)

2. **Cobertura:** Los tests cubren:
   - Happy path (casos exitosos)
   - Edge cases (límites)
   - Error cases (excepciones)
   - Casos especiales (Unicode, caracteres especiales)

3. **Performance:** Los tests deben ejecutarse en menos de 5 segundos

4. **Fixtures:** Se usan fixtures de pytest para:
   - Crear archivos temporales
   - Instanciar objetos
   - Proporcionar datos de prueba

---

## 🐛 Debugging

### Ver logs detallados
```bash
pytest -vv --tb=long
```

### Ejecutar un test específico
```bash
pytest tests/utils/test_document_loader.py::TestDocumentLoader::test_load_existing_file -v
```

### Mode watch (rerun en cambios)
```bash
pytest-watch
```

---

## 📞 Referencias

- [Pytest Documentation](https://docs.pytest.org/)
- [Pytest Fixtures](https://docs.pytest.org/en/stable/fixture.html)
- [Pytest Markers](https://docs.pytest.org/en/stable/example/markers.html)
