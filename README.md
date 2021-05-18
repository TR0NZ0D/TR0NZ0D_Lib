<h1>TR0NZ0D Lib</h1>
<hr>

<h3>What is?</h3>
<p>TR0NZ0D Lib is a library created in python to facilitate the use of some tools. The project is still under development, improvements and new features will be added. The main language of the project is portuguese, translations will be added in the future.</p>

<h3>Brief Documentation</h3>

<h4>Introduction</h4>
<p>Installing the library can be done by running the<code>pip install tr0nz0d</code>command on a terminal that has Python [3.8.x] installed.</p>

<h4>Methods</h4>
<h5><code>tr0nz0d.tools</code></h5>

- CPF

    Tools to generate, format and validate a cpf.

    * ``cpf.gerar()`` - Generates a mathematically valid cpf.<br>**Returns**
        - The plain cpf.

    * ``cpf.format(cpf: str)`` - Formats the cpf with the divisions.<br>**Returns**
        - The formatted cpf.

    * ``cpf.gerar_formatado()`` - Generates a mathematically valid cpf.<br>**Returns**
        - The formatted cpf.

    * ``cpf.validar()`` - Validates the mathematical authenticity of the CPF.<br>**Returns**
        - True [valid] or False [invalid]

- CNPJ

    Tools to generate, format and validate a cnpj.

    * ``cnpj.gerar()`` - Generates a mathematically valid cnpj.<br>**Returns**
        - The plain text.

    * ``cnpj.formatar(cnpj: str)`` - Formats the cnpj with the divisions.<br>**Returns**
        - The formatted cnpj.

    * ``cnpj.gerar_formatado()`` - Generates a mathematically valid cnpj.<br>**Returns**
        - The formatted cnpj.

    * ``cnpj.validar()`` - Validates the mathematical authenticity of the cnpj.<br>**Returns**
        - True [valid] or False [invalid]

- TEXT
    Tools to encapsulate and print text within a character set.

    * ``text.line_print(text: str, char_tl: str, char_md: str, char_tr: str, char_sides: str, char_bl: str, char_br: str)`` - Encapsulates a single-line text within the specified characters and print it.

    * ``text.text_print(text: str, char_tl: str, char_md: str, char_tr: str, char_sides: str, char_bl: str, char_br: str)`` - Encapsulates multiline text within characters specified and print it.

<h5><code>tr0nz0d.security</code></h5>

- CRIPTOGRAFIA
    Tools for encrypting and decrypting text.

    * ``criptografia.criptografar(text: str)`` - Encrypts past text.<br>**Returns**
        - List containing the encrypted text and the key.

    * ``criptografia.descriptografar(text: bytes)`` - Decrypts the text passed.<br>**Returns**
        - Decrypted literal text.

    * ``criptografia.descriptografar_com_chave(text: bytes, custom_key: bytes)`` - Decrypts the text passed using the specific key.<br>**Returns**
        - Decrypted literal text.

    * ``criptografia.get_key()`` - Returns the key used to encrypt the text.<br>**Returns**
        - Encryption key.

- PSWD

    Tools for creating complex passwords and codes.

    * ``pass.gerar(lenght: int)`` - Creates a complex code of determined length.<br>**Returns**
        - Code created in literal text.


<hr>