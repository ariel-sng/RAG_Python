## INGESTA DE ARCHIVOS

``uv run python -m src.scripts.run_ingestion documents/FAQ.txt --reload``


Fixed

Divide el texto en fragmentos de tamaño fijo.
Usa chunk_size y chunk_overlap para controlar cuánto mide cada chunk y cuánto se solapan.
Ideal cuando querés chunks uniformes sin depender de la estructura del texto.

Sentence

Divide el texto en oraciones y agrupa oraciones hasta acercarse al chunk_size.
No usa overlap, sino que mantiene unidades semánticas más naturales.
Bueno para textos largos donde querés preservar mejor el sentido del contenido.

Por defecto, si no se selecciona ningún ``--chunk-strategy``, es fixed por defecto

``uv run python -m src.scripts.run_ingestion documents/FAQ.txt --chunk-strategy sentence ``

## LEER CHUNKS DE CHROMADB

``uv run python -m src.scripts.read_chroma``

