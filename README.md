# Automação de E-mail + Streamlit 

Este repositório contém um projeto de automação que cria uma aplicação Streamlit a partir de uma base de dados recebida via e-mail. O objetivo é simplificar e automatizar o processo de visualização de dados, tornando-o mais eficiente e acessível.

O codigo de forma automática procura a base de dados dentro do seu e-mail.

## Descrição do Projeto
A automação realiza as seguintes etapas:

<ul>
        <li><strong>Recepção de E-mail:</strong> Recebe um e-mail contendo uma base de dados em anexo.</li>
        <li><strong>Processamento de Dados:</strong> Processa a base de dados e extrai as informações necessárias.</li>
        <li><strong>Criação de Aplicação:</strong> Cria uma aplicação Streamlit para visualização e análise dos dados.</li>
        <li><strong>Disponibilização:</strong> Disponibiliza a aplicação para acesso e uso.</li>
</ul>


## Importância da Automação na Recepção de E-mails : 
A automação na recepção de e-mails é fundamental para agilizar o fluxo de trabalho e garantir que os dados estejam sempre atualizados e disponíveis para análise. Com a automação, eliminamos a necessidade de verificar manualmente a caixa de entrada, baixar anexos e processar os dados. Isso não apenas economiza tempo, mas também reduz a possibilidade de erros humanos. A automação é configurada para procurar e-mails com um assunto específico e baixar automaticamente os anexos, garantindo que os dados sejam processados assim que chegam.

Para fins de desenvolvimento e teste, utilizei a biblioteca Faker para gerar dados fictícios e enviá-los para meu e-mail. O código foi configurado para procurar e-mails com o assunto contendo a palavra 'importante' e baixar o anexo desses e-mails.

![image](https://github.com/user-attachments/assets/d2005794-e9b7-4fdf-889d-23773748482a)

## Visualização dos Dados : 
A aplicação Streamlit é gerada para extrair as informações do arquivo em anexo e realizar algumas análises. Aqui estão alguns exemplos de visualizações geradas:
Gerando o streamlit para extrair as infomrmções no arquivo em anexo e gerando algumas análises:

![image](https://github.com/user-attachments/assets/9da0868f-b53d-4b93-a512-501c0892e1d3)

![image](https://github.com/user-attachments/assets/95ca38c4-04ad-4487-b2dd-f134212c7c81)

## Estrutura do Projeto : 
<pre>
.
├── email_read_class.py          # Script para processamento de e-mails
├── fake_data_generator.py       # Script para gerar dados fake com Faker
├── faker_users.csv              # Exemplo de base de dados fake
├── report_generate.py           # Script principal da aplicação Streamlit
├── data                         # Pasta onde o codigo salva o anexo do email
        ├── users.csv            # Base de dados que salvou do e-mail
└── README.md                    # Documentação do projeto
 </pre>


<h2>Gerando Dados Fake</h2>
    <p>Para gerar dados fake para testes, execute o script <code>fake_data_generator.py</code>:
        <pre><code>python fake_data_generator.py</code></pre>
    </p>

<h2>Executando a Aplicação</h2>
  <p>Para iniciar a aplicação Streamlit, execute o seguinte comando no diretório do projeto:
      <pre><code>streamlit run report_generate.py</code></pre>
    </p>
