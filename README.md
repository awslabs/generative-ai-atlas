## Generative AI Atlas
This repository contains the content and infrastructure of the Generative AI Atlas website.

### Contributing
Contributions are welcome! See [CONTRIBUTING](./CONTRIBUTING.md).

### Running Locally
- Clone the repo: 
  - `git clone https://github.com/awslabs/generative-ai-atlas.git`
- Switch directory: 
  - `cd generative-ai-atlas`
- Install uv (if not already installed):
  - `pip install uv`
- Create and activate a virtual environment:
  - `uv venv`
  - `source .venv/bin/activate`  # On Unix/macOS
  - `.venv\Scripts\activate`     # On Windows
- Install dependencies using uv: 
  - `uv sync`
  
Finally, launch the site locally using the `mkdocs serve` command from the root of the repo.

### Dependency Troubleshooting

The PDF plugin (mkdocs-to-pdf) uses WeasyPrint, which requires system-level libraries.

**macOS (Homebrew):**

```bash
brew install pango gdk-pixbuf libffi
```

On Apple Silicon, the dynamic linker may not find the Homebrew libraries automatically. If you see errors like `cannot load library 'libgobject-2.0-0'`, set the library path:

```bash
export DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib
```

Add this to your `~/.zshrc` to make it persistent. Then run `mkdocs serve` as usual.

**Other platforms:**

If you encounter dependency-related errors (e.g., `jpeg`, `cairo-2`, or other image processing libraries), refer to the [Material for MkDocs Image Processing Requirements](https://squidfunk.github.io/mkdocs-material/plugins/requirements/image-processing/) and [WeasyPrint installation docs](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation) for platform-specific instructions.

## License Summary

The documentation is made available under the Creative Commons Attribution-ShareAlike 4.0 International License. See the LICENSE file.

The sample code within this documentation is made available under the MIT-0 license. See the LICENSE-SAMPLECODE file.

## DISCLAIMER

1.	Generative AI Atlas (“ATLAS”) is provided for informational purposes only, and does not constitute legal, regulatory, compliance, or professional advice of any kind, and should not be relied upon as such. 
2.	You should consider performing your own independent assessment of the information and other content contained in ATLAS to ensure that your use complies with your own specific quality control practices and standards, as well as local rules, laws, regulations, licenses and terms of use that apply to you and your content.
