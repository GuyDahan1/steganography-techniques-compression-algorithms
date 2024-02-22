
# Advanced Image Processing and Encryption Techniques

This project showcases advanced techniques in image processing and encryption, including image encoding and decoding, DCT (Discrete Cosine Transform) processing, and secure encryption using Blowfish.

## Features

- **Image Encoding and Decoding**: Hide and retrieve messages within images using steganography.
- **DCT Image Processing**: Apply DCT and IDCT to images for processing.
- **Blowfish Encryption**: Securely encrypt and decrypt images with Blowfish cipher.

## Dependencies

- numpy
- rsa
- PIL (Python Imaging Library)
- scipy
- skimage
- pycrypto
- secrets
- base64

## Installation

Ensure you have Python installed on your system. Then, install the required dependencies:

```bash
pip install numpy rsa Pillow scipy scikit-image pycrypto
```

## Usage

### Image Encoding and Decoding

- **Encoding**: Hide a message within an image file.
- **Decoding**: Extract a hidden message from an image file.

### DCT Processing

Process an image using DCT to analyze or modify its frequency components.

### Blowfish Encryption

Encrypt and decrypt images for secure transmission or storage.

## Example

To encode a message within an image:

```python
Encode('source_image.png', 'Secret Message', 'dest_image.png', '1')
```

To decode a message from an image:

```python
Decode('dest_image.png')
```

To process an image using DCT:

```python
# Assumes image path is provided by the user
```

To encrypt and decrypt an image:

```python
# Convert image to data, then encrypt or decrypt
```


## Contributors

GUY DAHAN


