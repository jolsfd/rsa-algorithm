#!/usr/bin/env python3

import time
import platform
import cpuinfo
import examples

from rsa import RSA


class Benchmark:
    def __init__(self, n: int, e: int, d: int, m: int, c: int, text: str) -> None:
        self.n = n
        self.e = e
        self.d = d
        self.m = m
        self.c = c
        self.text = text

        self.rsa = RSA()

    def bench_encrypt(self, n: int) -> float:
        start = time.time()
        for i in range(n):
            self.rsa.encrypt(self.m, self.e, self.n)

        return time.time() - start

    def bench_decrypt(self, n: int) -> float:
        start = time.time()
        for i in range(n):
            self.rsa.decrypt(self.c, self.d, self.n)

        return time.time() - start

    def bench_encrypt_text(self, n: int) -> float:
        start = time.time()
        for i in range(n):
            self.text_c = self.rsa.encrypt_text(self.text, self.d, self.n)

        return time.time() - start

    def bench_decrypt_text(self, n: int) -> float:
        start = time.time()
        for i in range(n):
            self.rsa.decrypt_text(self.text_c, self.d, self.n)

        return time.time() - start


if __name__ == "__main__":
    m = examples.m_4096
    c = examples.c_4096

    text = """Die Kryptographie ist eine Wissenschaft, die sich mit den Methoden beschäftigt, die durch Verschlüsselung und verwandte Verfahren Daten vor unbefugtem Zugriff schützen sollen. Das eine wichtige Hilfsmittel der Kryptographie ist die Matehmatik, denn nur durch mathematische Denkweise und mithilfe von mathematischen Kenntnissen ist es möglich, Verfahren zur sicheren Verschlüsselung zu entwickeln. Das andere wichtige Hilfsmittel ist der Computer. Dieser führt die Verschlüsselungsverfahren aus und leistet wichtige Dienste bei der Untersuchung von kryptografischen Methoden und Schwachstellen."""

    # Symsteminformationen
    print("=" * 40, "System Information", "=" * 40)
    computer = platform.uname()
    print(f"System: {computer.system}")
    print(f"Node Name: {computer.node}")
    print(f"Release: {computer.release}")
    print(f"Version: {computer.version}")
    print(f"Processor: {computer.processor}")
    print()

    # CPU Information
    print(f"=" * 40, "CPU Information", "=" * 40)
    info = cpuinfo.get_cpu_info()
    name = info["brand_raw"]
    cores = info["count"]
    print(f"Name: {name}")
    print(f"CPU Cores: {cores}")
    print()

    # Python Information
    print("=" * 40, "Python Information", "=" * 40)
    print(f"Version: {platform.python_version()}")
    print(f"Compiler: {platform.python_compiler()}")
    print()

    # Treiber Code
    count = 100
    print(f"Running Benchmark {count} times...")
    bench = Benchmark(examples.n_4096, examples.e_4096, examples.d_4096, m, c, text)

    time_decrypt = bench.bench_encrypt(count)
    print(f"{time_decrypt}s for encryption.")

    time_encrypt = bench.bench_decrypt(count)
    print(f"{time_encrypt}s for decryption.")

    time_decrypt_text = bench.bench_encrypt_text(count)
    print(f"{time_decrypt_text}s for text encryption.")

    time_encrypt_text = bench.bench_decrypt_text(count)
    print(f"{time_encrypt_text}s for text decryption.")
