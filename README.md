# Python RPC (Remote Procedure Call)

**Serviço de Cálculo de IMC**
Método no Servidor:

Nome do Método: ```exposed_calculate_imc```
Parâmetros:
```weight```: Peso da pessoa em quilogramas (float).
```height```: Altura da pessoa em metros (float).
Utilização:

Chame o método ```exposed_calculate_imc``` do servidor RPC, fornecendo o peso e a altura como argumentos. O método retornará o valor do IMC calculado com base nos valores fornecidos.

**Serviço de Resolução de Equações de Segundo Grau**
Método no Servidor:

Nome do Método: ```exposed_calculate_quadraticEquation```
Parâmetros:
```a```: Coeficiente 'a' da equação de segundo grau (float). Não pode ser zero.
```b```: Coeficiente 'b' da equação de segundo grau (float).
```c```: Coeficiente 'c' da equação de segundo grau (float).
Utilização:

Chame o método ```exposed_calculate_quadraticEquation``` do servidor RPC, fornecendo os coeficientes 'a', 'b' e 'c' da equação de segundo grau como argumentos. O método retornará as raízes da equação, que podem ser:
Uma única raiz real, se o discriminante for zero.
Duas raízes reais, se o discriminante for positivo.
Duas raízes complexas, se o discriminante for negativo.

**Serviço de Verificação de Palíndromos**
Método no Servidor:

Nome do Método: ```exposed_check_palindrome```
Parâmetros:
```word```: A palavra que você deseja verificar como um palíndromo (string).
Utilização:

Chame o método ```exposed_check_palindrome``` do servidor RPC, fornecendo a palavra que você deseja verificar como argumento. O método retornará ```True``` se a palavra for um palíndromo e ```False``` caso contrário.

Lembre-se de que você precisa ter o servidor RPC em execução e ter uma conexão estabelecida a ele a partir do cliente para utilizar esses serviços. Certifique-se de configurar e executar o servidor RPC antes de chamar esses métodos em seu cliente.

# Tutorial

**Instalar a biblioteca ```RPyC``` (se ainda não estiver instalada):**
Certifique-se de que a biblioteca ```RPyC``` esteja instalada em seu ambiente Python. Você pode instalar usando o pip: ```pip install rpyc```

**Cole seu código do servidor em um arquivo:**
Cole todo o código do servidor em um arquivo Python. Por exemplo, você pode criar um arquivo chamado server.py e colar o código nele.

**Executar o servidor:**
Abra um terminal ou prompt de comando e navegue até o diretório onde o arquivo server.py está localizado. Em seguida, execute o servidor usando o seguinte comando: ```python server.py``` ou ```py server.py``` se estiver utilizando Windows.
Isso iniciará o servidor RPC na interface '0.0.0.0' (ou seja, estará disponível em todas as interfaces de rede) e na porta 18812, conforme definido em seu código. Certifique-se de que o servidor esteja em execução e que não haja erros.

**O servidor está pronto para receber conexões:**
Após iniciar o ```servidor```, ele estará pronto para receber conexões de clientes que desejam usar os serviços implementados.

Agora que o servidor está em execução, você pode criar um ```cliente``` (um programa Python separado) que se conecte ao servidor e chame os métodos ```RPC```, conforme explicado na resposta anterior.

Certifique-se de que o ```cliente``` esteja configurado para se conectar ao endereço ```'localhost'``` (ou o endereço onde o ```servidor``` está sendo executado) na porta 18812 (a mesma porta que o ```servidor``` está ouvindo). Quando o cliente se conecta ao servidor, ele pode chamar os métodos ```exposed_calculate_imc```, ```exposed_calculate_quadraticEquation``` e ```exposed_check_palindrome``` como mencionado na resposta anterior para usar os serviços do ```servidor RPC```.

**Encerrar o servidor:**
Para encerrar o servidor ```RPC``` que você configurou e está em execução, você pode fazê-lo manualmente ao pressionar ```Ctrl+C``` no ```terminal``` onde o servidor está em execução. Isso enviará um sinal de interrupção para o ```servidor``` e encerrará a execução do programa do ```servidor```.
