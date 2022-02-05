# RSA-Algorithm

## Installation

Clone the repository.
```bash
git clone https://github.com/jolsfd/rsa-algorithm.git
```

Install [Python 3.10](https://python.org) and the required modules. Decide if you want to use a venv. You can make a venv with ```python -m venv venv``` or ```make virtual_env``` and activate the venv with ```source venv/bin/activate```.
```bash
# With pip
pip install -r requirements.txt
# or
make install
```
## Test

Test the algorithm.
```bash
python test_rsa.py
# or
make test
```

## Benchmark

Benchmark the algorithm.
```bash
python bench_rsa.py
# or
make bench
```

## Command Line Interface

For creating a RSA key with a certain key lenght use the ```generate``` command.
```bash
# Example (Default: 2048)
python cli_rsa.py generate --bits 512
```

You can specifie where the key file should be saved with the ```--file``` flag before the command.
```bash
# Example (Default: key.txt)
python cli_rsa.py --file hello.txt generate
```

To encrypt a message use the ```encrypt``` command.
```bash
python cli_rsa.py encrypt "Hello World"
```

Copy the output and save it or decrypt it with the ```decrypt``` command by pasting the output after the command.
```bash
# Example
python cli_rsa.py decrypt 51895113689204577206839395581904075220
```