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

If you encounter dependency-related errors during setup (e.g., `jpeg`, `cairo-2`, or other image processing libraries), please refer to the [Material for MkDocs Image Processing Requirements](https://squidfunk.github.io/mkdocs-material/plugins/requirements/image-processing/) documentation for platform-specific installation instructions.

Common errors include:
- `The headers or library files could not be found for jpeg`
- `no library called "cairo-2" was found`
- Missing `pango` or `gdk-pixbuf` dependencies

The above documentation provides comprehensive guidance for resolving these issues on various operating systems.

## License Summary

The documentation is made available under the Creative Commons Attribution-ShareAlike 4.0 International License. See the LICENSE file.

The sample code within this documentation is made available under the MIT-0 license. See the LICENSE-SAMPLECODE file.

## DISCLAIMER

1.	Generative AI Atlas (“ATLAS”) is provided for informational purposes only, and does not constitute legal, regulatory, compliance, or professional advice of any kind, and should not be relied upon as such. 
2.	You should consider performing your own independent assessment of the information and other content contained in ATLAS to ensure that your use complies with your own specific quality control practices and standards, as well as local rules, laws, regulations, licenses and terms of use that apply to you and your content.
