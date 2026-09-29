import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from fpdf import FPDF


# 1. CONFIGURAÇÕES INICIAIS

load_dotenv()

st.set_page_config(page_title="DUA-ICL Planner", layout="wide", page_icon="🎓")

Banco_de_exemplos = {


    # EXEMPLO 1 — MÚLTIPLOS PERFIS


    "Múltiplos Perfis": """
### EXEMPLO ICL — Perfil: Múltiplos Perfis (TDAH + Dislexia + Turma Geral)
**ENTRADA:**
- Disciplina: História | Tópico: Abolição da Escravatura no Brasil | Série: 8º Ano EF
- Objetivos: Compreender os principais atores sociais e eventos que levaram à Lei Áurea (1888)
- Habilidades BNCC: (EF08HI14) Discutir a importância da participação da população negra na construção da identidade nacional brasileira; (EF08HI15) Identificar os processos de resistência dos escravizados no Brasil.
- Duração: 100 minutos
- Recursos Disponíveis: Computadores, Datashow, Cartões visuais, Textos impressos adaptados
 
**SAÍDA ESPERADA (Plano DUA):**
 
**Nome do Plano de Aula:** "Vozes da Liberdade: Os Caminhos para a Lei Áurea"
**Ano de Ensino:** 8º Ano do Ensino Fundamental II
**Habilidades BNCC:** (EF08HI14) Discutir a importância da participação da população negra, quilombola e de aliados no processo abolicionista; (EF08HI15) Identificar os processos de resistência dos escravizados no Brasil.
**Objetivos Gerais:** Compreender os principais agentes sociais, resistências e eventos que culminaram na Lei Áurea (1888), desenvolvendo leitura crítica de fontes históricas por meio de múltiplos suportes.
 
---
 
### Proposta de Dinâmica (Estrutura Geral)
- **Abertura Multimodal:** A aula inicia com mapa visual cronológico dos eventos (1850–1888) projetado no Datashow. O professor apresenta verbalmente o roteiro dos blocos de tempo (âncora para TDAH) e o vocabulário histórico-chave (beneficia todos).
- **Saneamento de Vocabulário:** Definição prévia e visual dos termos "abolição", "quilombo", "abolicionista", "escravizado" — cada termo associado a uma imagem histórica real projetada.
- **Critério de Agrupamento:** Trios com diferentes perfis de fluência leitora e atenção. A rotação de funções (ledor, anotador, apresentador) ocorre a cada atividade — nenhum papel é fixado por diagnóstico.
- **Monitoramento:** O professor observa se algum membro do trio está assumindo todas as funções. Se isso ocorrer, intervém redistribuindo explicitamente: "Agora é a vez de [nome] ser o ledor."
- **Gestão do Tempo:** Blocos de 15 min com cronômetro visual projetado (beneficia TDAH e toda a turma). Aviso verbal de 2 min antes de cada transição.
 
---
 
### Atividades Detalhadas e Focos do DUA
 
#### FOCO 1: PROPORCIONAR O ACESSO (Ativação e Sensibilização)
- **Atividade 1: Linha do Tempo Viva (15 min)**
  - **Barreira Identificada:** Textos densos de abertura bloqueiam o engajamento inicial de alunos com dislexia e dispersam alunos com TDAH antes do conteúdo começar.
  - **Descrição:** O professor projeta uma linha do tempo visual com os 5 eventos principais (1850–1888). Para cada evento, exibe uma imagem de época e faz uma pergunta oral à turma: "O que vocês acham que aconteceu aqui?"
  - **Acessibilidade (TDAH):** Blocos de 15 min com Time Timer projetado. Perguntas orais mantêm o engajamento ativo sem exigir leitura silenciosa prolongada.
  - **Acessibilidade (Dislexia):** Informação transmitida predominantemente por imagem + fala. Nenhum texto escrito é exigido neste momento.
  - **Acessibilidade (Turma Geral):** A discussão oral ativa o conhecimento prévio de todos e nivelar o ponto de partida sem depender de leitura prévia em casa.
  - **Materiais:** Slides com linha do tempo visual, imagens históricas de domínio público, cronômetro visual projetado (ex: Time Timer Online — gratuito).
  - **Critério de Avaliação:** O aluno consegue, oralmente, associar ao menos 1 evento a uma data ou personagem histórico — participação oral tem o mesmo peso que resposta escrita.
 
#### FOCO 2: PROPORCIONAR A PRÁTICA GUIADA (Desenvolvimento e Colaboração)
- **Atividade 2a: Análise de Fontes em Trio (25 min)**
  - **Barreira Identificada:** Fontes históricas em formato exclusivamente textual excluem alunos com dislexia do processo de análise crítica — a barreira está no suporte, não na capacidade de raciocínio histórico.
  - **Descrição:** Cada trio recebe um envelope com 3 fontes sobre o mesmo evento abolicionista: (a) trecho de texto adaptado, (b) imagem histórica com legenda curta, (c) QR Code para podcast narrado de 2 min. O trio decide coletivamente qual fonte explorar primeiro.
  - **Acessibilidade (Dislexia):** Texto adaptado em Arial 14, fundo creme, parágrafos de no máximo 5 linhas. O podcast elimina completamente a barreira de decodificação.
  - **Acessibilidade (TDAH):** A escolha da sequência de exploração pelo próprio trio aumenta o engajamento autônomo e a sensação de controle.
  - **Acessibilidade (Turma Geral):** Três suportes distintos para o mesmo conteúdo permitem que cada aluno acesse pela via de maior fluência.
  - **Materiais:** Envelopes com 3 tipos de fonte por evento, textos adaptados (Arial 14, fundo creme), QR Codes para podcasts narrados gratuitos (Radioagência Nacional).
  - **Critério de Avaliação:** O trio preenche conjuntamente uma ficha de 3 campos: "Quem são os personagens?", "O que aconteceu?", "Por que foi importante?" — aceita resposta por palavras-chave, frase ou desenho.
 
- **Atividade 2b: Construção Colaborativa do Mapa de Resistências (20 min)**
  - **Barreira Identificada:** A síntese de informações de múltiplas fontes exige função executiva de organização — área de dificuldade específica para TDAH.
  - **Descrição:** Com base nas fichas preenchidas, cada trio constrói coletivamente um mapa visual conectando os eventos e personagens estudados. O professor disponibiliza um template de mapa com nós já rotulados (personagens centrais) para grupos que precisam de mais estrutura.
  - **Acessibilidade (TDAH):** Template de mapa pré-estruturado reduz a demanda de organização executiva. O professor oferece o template proativamente — não como "versão mais fácil", mas como "opção de organização".
  - **Acessibilidade (Dislexia):** O mapa é predominantemente visual; legendas curtas substituem textos corridos.
  - **Acessibilidade (Turma Geral):** Trios que não precisam do template são desafiados a criar a estrutura do mapa do zero.
  - **Materiais:** Folhas A3, canetões coloridos, template de mapa impresso (opcional).
  - **Critério de Avaliação:** O mapa conecta ao menos 3 eventos ou personagens com uma relação causal identificável ("X lutou contra Y porque...").
 
#### FOCO 3: PROPORCIONAR A PRÁTICA AUTÔNOMA (Internalização e Expressão)
- **Atividade 3: Produção Multimodal — "Minha Voz sobre a Abolição" (30 min)**
  - **Barreira Identificada:** Avaliação exclusivamente escrita impede que alunos com dislexia demonstrem o conhecimento histórico adquirido — a barreira está no formato de expressão, não no conteúdo aprendido.
  - **Descrição:** Individualmente, cada aluno escolhe um formato para registrar o que aprendeu sobre o evento estudado pelo seu trio. O professor apresenta os formatos sem hierarquizá-los.
  - **Acessibilidade (Dislexia / TDAH / Turma Geral):**
    - Formato A — Texto escrito: 5 a 8 linhas no caderno ou Google Docs.
    - Formato B — Gravação de voz: 1–2 min explicando o evento (app de gravação nativo — gratuito).
    - Formato C — Infográfico desenhado: linha do tempo pessoal com imagens e legendas curtas.
  - **Monitoramento:** O professor circula observando se algum aluno está travado na escolha do formato. Se sim, apresenta os três formatos novamente de forma individual e pergunta: "Qual desses parece mais fácil para você começar agora?"
  - **Materiais:** Computadores com Google Docs, app de gravação nativo do sistema, folhas A3.
  - **Critério de Avaliação:** O produto final (em qualquer formato) inclui: ao menos 1 personagem histórico, 1 evento-chave e uma relação causal ("isso aconteceu porque..."). A avaliação incide sobre o conteúdo histórico — o formato não é critério.
 
---

""",


    # EXEMPLO 2 — TDAH

    "TDAH": """
### EXEMPLO ICL — Perfil: TDAH
**ENTRADA:**
- Disciplina: Matemática | Tópico: Frações | Série: 6º Ano EF
- Objetivos: Compreender o conceito de fração como parte de um todo
- Habilidades BNCC: (EF06MA07) Compreender, comparar e ordenar frações associadas às ideias de partes de inteiros.
- Duração: 50 minutos
- Recursos Disponíveis: Material concreto (blocos fracionários), Computadores, Projetor (Datashow)
 
**SAÍDA ESPERADA (Plano DUA):**
 
**Nome do Plano de Aula:** "Fracionando o Todo: Divisão Prática"
**Ano de Ensino:** 6º Ano do Ensino Fundamental II
**Habilidades BNCC:** (EF06MA07) Compreender, comparar e ordenar frações associadas às ideias de partes de inteiros, usando a reta numérica como representação.
**Objetivos Gerais:** Compreender o conceito de fração como parte de um todo, identificando numeradores e denominadores através de associações concretas, visuais e digitais.
 
---
 
### Proposta de Dinâmica (Estrutura Geral)
- **Rotina Sem Medos:** O professor apresenta visualmente o cronograma da aula no projetor, dividindo-a em blocos de 10 minutos com Time Timer projetado.
- **Saneamento de Vocabulário:** Definição prévia dos termos "fração", "numerador" e "denominador" com imagem associada antes de qualquer atividade prática.
- **Critério de Agrupamento:** Duplas com diferentes níveis de fluência matemática. Um aluno apoia o outro sem fazer a atividade por ele.
- **Monitoramento:** Se o aluno mais avançado estiver resolvendo sozinho, o professor intervém: "Mostre para seu colega onde você está olhando, não dê a resposta."
- **Gestão do Tempo:** Blocos de 10 min com cronômetro visual. Aviso de 2 min antes de cada transição.
 
---
 
### Atividades Detalhadas e Focos do DUA
 
#### FOCO 1: PROPORCIONAR O ACESSO (Ativação e Sensibilização)
- **Atividade 1: Desafio do Todo Inteiro (10 min)**
  - **Barreira Identificada:** Abstrações matemáticas sem ancoragem concreta perdem a atenção de alunos com TDAH nos primeiros minutos — o engajamento inicial precisa ser físico e imediato.
  - **Descrição:** O professor divide fisicamente um objeto inteiro (pizza de papelão) na frente da turma e pergunta: "Quantas partes ficaram? Como chamamos uma dessas partes?"
  - **Acessibilidade (TDAH):** Manipulação física do objeto e pergunta direta mantêm o engajamento ativo. O aluno escolhe se prefere manusear o material ou acompanhar pelo projetor.
  - **Acessibilidade (Turma Geral):** A divisão física torna o conceito abstrato de fração concreto e acessível para todos.
  - **Materiais:** Pizza de papelão fracionada, projetor com Time Timer.
  - **Critério de Avaliação:** O aluno consegue nomear, com ou sem apoio, o numerador ou o denominador da fração representada pelo objeto dividido.
 
#### FOCO 2: PROPORCIONAR A PRÁTICA GUIADA (Desenvolvimento e Colaboração)
- **Atividade 2: Estações de Aprendizagem Colaborativa (25 min)**
  - **Barreira Identificada:** Atividades longas e lineares esgotam a capacidade atencional de alunos com TDAH — a variação de suporte (concreto/digital) a cada rotação renova o engajamento.
  - **Descrição:** Em duplas, os alunos alternam entre:
    1) *Mesa Concreta (12 min):* Montar frações usando blocos fracionários geométricos.
    2) *Mesa Digital (13 min):* Resolver 3 desafios gamificados no Khan Academy.
  - **Acessibilidade (TDAH):** Rotação entre mesas mantém novidade sensorial. O professor circula oferecendo pistas visuais no erro: "Olhe para o número de baixo — quantas partes no total?"
  - **Acessibilidade (Turma Geral):** A dupla colaborativa permite que alunos com diferentes ritmos se apoiem mutuamente.
  - **Materiais:** Blocos fracionários coloridos, computadores/tablets com Khan Academy.
  - **Critério de Avaliação:** A dupla monta corretamente ao menos 2 das 3 frações solicitadas na mesa concreta. O professor registra se o acerto ocorreu com pista visual, com apoio do colega ou de forma autônoma.
 
#### FOCO 3: PROPORCIONAR A PRÁTICA AUTÔNOMA (Internalização e Expressão)
- **Atividade 3: Registro do Aprendizado (15 min)**
  - **Barreira Identificada:** Exigir um único formato escrito de registro ao final da aula penaliza alunos com TDAH que esgotaram a capacidade de escrita prolongada — mas têm o conceito internalizado.
  - **Descrição:** O aluno registra o conceito de uma fração à sua escolha. Ficha-resumo visual fixada na lousa. Ao final, o professor conduz uma autoavaliação rápida oral: "O que eu aprendi hoje? O que ainda tenho dúvida?"
  - **Acessibilidade (TDAH):** Três opções de expressão sem hierarquia: escrita no caderno, desenho da representação geométrica, ou explicação em áudio gravada no app nativo do computador.
  - **Acessibilidade (Turma Geral):** A autoavaliação oral final beneficia toda a turma, não só o aluno com TDAH.
  - **Materiais:** Ficha-resumo visual na lousa, papel sulfite, app de gravação nativo (gratuito).
  - **Critério de Avaliação:** O registro (em qualquer formato) identifica corretamente numerador e denominador de uma fração. Com apoio da ficha-resumo é suficiente para avaliação positiva.
 
---

""",


    # EXEMPLO 3 — TEA (Autismo)


    "TEA (Autismo)": """
### EXEMPLO ICL — Perfil: TEA (Autismo)
**ENTRADA:**
- Disciplina: Computação | Tópico: Arquitetura de Computadores (Memórias) | Série: 1º Ano Ensino Médio
- Objetivos: Compreender a hierarquia de memórias (Registradores, Cache, RAM e HD) e suas propriedades de velocidade e capacidade.
- Habilidades BNCC: (EF09CO12) Compreender os princípios de funcionamento dos componentes de hardware e sistemas operacionais.
- Duração: 50 minutos
- Recursos Disponíveis: Componentes de hardware reais descartados (pentes de RAM, placas-mãe, HDs), simulador web, cartões visuais de rotina, computadores.
 
**SAÍDA ESPERADA (Plano DUA):**
 
**Nome do Plano de Aula:** "Velocidade vs. Capacidade: A Hierarquia de Memórias"
**Ano de Ensino:** 1º Ano do Ensino Médio
**Habilidades BNCC:** (EF09CO12) Compreender os princípios de funcionamento dos componentes de hardware.
**Objetivos Gerais:** Identificar a função de cada nível da hierarquia de memórias, correlacionando capacidade de armazenamento e velocidade de acesso por meio de exploração física concreta, representação em múltiplos formatos e suporte analítico estruturado.
 
---
 
### Proposta de Dinâmica (Estrutura Geral)
- **Previsibilidade de Rotina:** A aula inicia com o roteiro visual das atividades estruturado em blocos de tempo fixos projetados no Datashow. Avisos de transição ocorrem sempre com 2 minutos de antecedência usando um cronômetro digital na tela.
- **Saneamento de Vocabulário:** Definição literal e direta de termos técnicos ("volatilidade", "latência", "largura de banda") em um glossário digital ou impresso permanente na bancada, evitando analogias abstratas ambíguas.
- **Pausa de Regulação:** Pausa estruturada de 3 minutos para regulação cognitiva e sensorial após a atividade prática. O estudante pode optar por permanecer em silêncio, utilizar fones de ouvido ou interagir livremente com componentes físicos neutros na bancada de materiais.
- **Critério de Agrupamento:** Trabalho individual ou em dupla de escolha livre baseada em afinidade prévia. A preferência por realizar a tarefa individualmente é sempre respeitada sem necessidade de justificativa para evitar sobrecarga de interação social.
- **Monitoramento:** O professor circula discretamente na sala prestando apoios individuais apenas sob demanda ou apontando pistas visuais, evitando interrupções verbais abruptas que quebrem o hiperfoco.
 
---
 
### Atividades Detalhadas e Focos do DUA
 
#### FOCO 1: PROPORCIONAR O ACESSO (Ativação e Sensibilização)
- **Atividade 1: Desconstrução de Hardware na Mesa (15 min)**
  - **Barreira Identificada:** Explicar a hierarquia de memórias de forma puramente teórica ou abstrata gera barreiras de processamento visual e desinteresse para alunos dentro do espectro autista.
  - **Descrição:** O professor disponibiliza nas mesas de trabalho componentes físicos reais descartados (módulos de memória RAM, discos rígidos abertos e processadores antigos). Os alunos tocam e examinam os componentes enquanto acompanham uma breve apresentação visual no projetor correlacionando o tamanho físico de cada peça à sua posição no computador.
  - **Acessibilidade (TEA):** O contato tátil direto com o hardware real ancora o conceito abstrato em um elemento físico concreto de alto interesse e foco. Instruções de exploração são diretas e quantificadas: "Encontre 3 conexões metálicas na placa".
  - **Acessibilidade (Turma Geral):** A manipulação física das peças desmistifica a parte interna de um computador para todos os estudantes, nivelando a turma na prática.
  - **Materiais:** Componentes de hardware reais descartados (RAM, HD, CPU), projetor de slides.
  - **Critério de Avaliação:** O estudante aponta ou indica fisicamente (usando as peças da mesa) qual componente é responsável por armazenar dados temporariamente e qual armazena de forma permanente.
 
#### FOCO 2: PROPORCIONAR A PRÁTICA GUIADA (Desenvolvimento e Colaboração)
- **Atividade 2: Mapeamento de Propriedades com Suporte Físico-Digital (17 min)**
  - **Barreira Identificada:** Tarefas de desenho livre ou redação aberta para explicar a diferença entre memórias geram alta ansiedade de iniciação e dificuldade de estruturação lógica.
  - **Descrição:** Os estudantes organizam os componentes de memória em uma pirâmide hierárquica baseada em velocidade e capacidade. Para estruturar a montagem, o estudante pode optar por usar um template gráfico impresso com lacunas bem definidas ou um simulador de arrastar e soltar no computador.
  - **Acessibilidade (TEA):** O template visual e estruturado de pirâmide fornece limites claros de onde colocar cada resposta, reduzindo a ansiedade de folha em branco. O professor oferece opções com níveis graduais de suporte visual (com ou sem dicas de tamanhos e velocidades nas lacunas).
  - **Acessibilidade (Turma Geral):** A escolha entre usar o simulador digital no computador ou o modelo impresso em papel atende a diferentes estilos de aprendizagem e preferências da turma.
  - **Materiais:** Templates físicos de pirâmide de memória, computadores com acesso ao simulador web, etiquetas adesivas organizadoras.
  - **Critério de Avaliação:** O estudante (ou dupla) posiciona corretamente ao menos 3 níveis da hierarquia de memórias em relação ao custo e velocidade utilizando o suporte escolhido.
 
*[PAUSA SENSORIAL — 3 min — fone de ouvido / silêncio / manipulação física neutra]*
 
#### FOCO 3: PROPORCIONAR A PRÁTICA AUTÔNOMA (Internalização e Expressão)
- **Atividade 3: Análise de Cenário com Checklist de Decisão (15 min)**
  - **Barreira Identificada:** Questionamentos abertos sobre "o que você faria para melhorar o computador?" geram ambiguidade, travamento ou respostas curtas demais por falta de critérios de conclusão claros.
  - **Descrição:** O estudante atua de forma autônoma como um técnico de computadores resolvendo um caso de atualização (ex: "O computador de um escritório demora 5 minutos para ligar. Qual memória precisa de upgrade?"). Ele analisa o problema usando um checklist plastificado de 3 etapas que guia o diagnóstico passo a passo.
  - **Acessibilidade (TEA):** O checklist transforma a resolução de problemas em um fluxo de análise preditivo, concreto e estruturado, definindo de maneira explícita o momento em que a tarefa é considerada finalizada.
  - **Acessibilidade (Turma Geral):** O checklist de análise apoia as funções executivas e de organização de escrita de todos os alunos durante o diagnóstico.
  - **Materiais:** Estudo de caso impresso/digital, checklist plastificado com critérios de tomada de decisão, caneta de quadro branco para marcação.
  - **Critério de Avaliação:** O estudante completa corretamente a análise do caso seguindo as etapas do checklist, identificando o gargalo de hardware de forma coerente.
 
---
""",


    # EXEMPLO 4 — DISLEXIA

    "Dislexia": """
### EXEMPLO ICL — Perfil: Dislexia
**ENTRADA:**
- Disciplina: Ciências | Tópico: Sistema Solar | Série: 5º Ano EF
- Objetivos: Identificar os planetas e suas características básicas
- Habilidades BNCC: (EF05CI10) Identificar algumas constelações no céu e os planetas como corpos celestes do Sistema Solar; (EF05CI11) Associar o movimento diário do Sol e demais estrelas no céu ao movimento de rotação da Terra.
- Duração: 90 minutos
- Recursos Disponíveis: Vídeos narrados, Textos impressos com formatação acessível, Banco de palavras físico, Computadores
 
**SAÍDA ESPERADA (Plano DUA):**
 
**Nome do Plano de Aula:** "Viajando pelo Sistema Solar: Cores e Texturas"
**Ano de Ensino:** 5º Ano do Ensino Fundamental I
**Habilidades BNCC:** (EF05CI10) Identificar as constelações e os planetas como corpos celestes do Sistema Solar; (EF05CI11) Associar movimentos celestes ao movimento de rotação da Terra.
**Objetivos Gerais:** Identificar a ordem e as características básicas dos planetas do Sistema Solar utilizando suportes visuais, auditivos e textuais acessíveis.
 
---
 
### Proposta de Dinâmica (Estrutura Geral)
- **Acolhimento de Linguagem:** A introdução prioriza canais visuais e auditivos — nenhum texto é exigido na abertura da aula.
- **Esclarecimento Terminológico:** Termos científicos ("órbita", "gravidade", "gasoso") são definidos previamente com imagem associada e fixados em cartaz visual na lousa durante toda a aula.
- **Critério de Agrupamento:** Duplas com fluência leitora variada. O papel de ledor é rotativo a cada atividade — nenhum aluno é identificado como "o que precisa de ajuda" e todos assumem ambos os papéis.
- **Monitoramento:** O professor observa se o papel de ledor está sendo evitado por algum membro. Se sim, intervém de forma privada: "Agora é sua vez de ler para o seu colega — pode apontar com o dedo enquanto lê."
- **Gestão do Tempo:** A aula de 90 min é dividida em 4 blocos explícitos no cronograma visual projetado.
 
---
 
### Atividades Detalhadas e Focos do DUA
 
#### FOCO 1: PROPORCIONAR O ACESSO (Ativação e Sensibilização)
- **Atividade 1: Imersão Audiovisual no Espaço (20 min)**
  - **Barreira Identificada:** Textos introdutórios densos bloqueiam o acesso ao conteúdo científico para alunos com dislexia antes mesmo de a aula começar — a barreira está no canal de entrada, não na capacidade de compreensão.
  - **Descrição:** Exibição de vídeo narrado de 5 min sobre os planetas, seguida de discussão oral coletiva mediada pelo professor para levantar conhecimentos prévios sem exigir leitura.
  - **Acessibilidade (Dislexia):** Substituição total de texto introdutório por áudio e vídeo. As contribuições orais dos alunos têm o mesmo peso epistêmico que respostas escritas.
  - **Acessibilidade (Turma Geral):** A discussão oral ativa o conhecimento prévio de todos e cria base compartilhada para as atividades seguintes.
  - **Materiais:** Datashow, caixas de som, vídeo sobre o Sistema Solar (canal NASA em Português ou Khan Academy — gratuito).
  - **Critério de Avaliação:** O aluno nomeia oralmente ao menos 2 planetas ou características observadas no vídeo.
 
#### FOCO 2: PROPORCIONAR A PRÁTICA GUIADA (Desenvolvimento e Colaboração)
- **Atividade 2a: Mapeamento Visual dos Planetas (25 min)**
  - **Barreira Identificada:** Fichas com texto em fonte padrão e papel branco de alto contraste aumentam a fadiga visual e os erros de decodificação em alunos com dislexia — o problema está no design do material, não na capacidade cognitiva.
  - **Descrição:** Em duplas (com ledor rotativo), os alunos recebem fichas dos planetas para organizar por ordem de proximidade do Sol.
  - **Acessibilidade (Dislexia):** Fichas em papel creme, fonte OpenDyslexic ou Arial 14, parágrafos de no máximo 3 linhas. Banco de Palavras físico disponível na mesa para apoio ortográfico. O professor intervém apontando o mapa da lousa para comparação visual.
  - **Acessibilidade (Turma Geral):** O banco de palavras e o mapa da lousa são recursos disponíveis para todos — não sinalizam diagnóstico.
  - **Materiais:** Fichas adaptadas (fundo creme, Arial 14), banco de palavras, mapa visual do Sistema Solar na lousa.
  - **Critério de Avaliação:** A dupla organiza corretamente ao menos 5 dos 8 planetas. O professor registra as estratégias de leitura observadas (uso do banco de palavras, apontamento, leitura em voz baixa).
 
- **Atividade 2b: Ficha de Características Guiada (20 min)**
  - **Barreira Identificada:** Escrever características a partir de um texto corrido exige decodificação e produção simultâneas — dupla demanda que pode bloquear o aluno com dislexia mesmo quando ele compreendeu o conteúdo.
  - **Descrição:** Cada dupla escolhe 2 planetas e preenche uma ficha estruturada com campos: nome do planeta, tamanho (grande/médio/pequeno), tipo (rochoso/gasoso), curiosidade. Os campos têm exemplos preenchidos na primeira linha como modelo.
  - **Acessibilidade (Dislexia):** A ficha estruturada separa a tarefa de "compreender" da tarefa de "redigir". O exemplo preenchido na primeira linha mostra o nível de detalhe esperado sem exigir inferência.
  - **Acessibilidade (Turma Geral):** A estrutura da ficha organiza o pensamento de todos os alunos, não só dos que têm dislexia.
  - **Materiais:** Fichas estruturadas com campos e exemplo preenchido, banco de palavras.
  - **Critério de Avaliação:** A dupla preenche ao menos 3 dos 4 campos para os 2 planetas escolhidos — com apoio do banco de palavras e da ficha-modelo é suficiente para avaliação positiva.
 
#### FOCO 3: PROPORCIONAR A PRÁTICA AUTÔNOMA (Internalização e Expressão)
- **Atividade 3: Relato de Descobertas Científicas (20 min)**
  - **Barreira Identificada:** Avaliações exclusivamente escritas com tempo rígido penalizam alunos com dislexia pela velocidade de escrita, não pelo conhecimento científico — a barreira está no formato de entrega, não no conteúdo aprendido.
  - **Descrição:** Individualmente, cada aluno escolhe um planeta e registra suas 2 principais características no formato de sua preferência. O professor apresenta os formatos sem hierarquizá-los: "Todos esses formatos valem igual."
  - **Acessibilidade (Dislexia / Turma Geral):**
    - Formato A — Escrita: digitação no Google Docs com leitura em voz alta nativa (Ferramentas > Acessibilidade — gratuito).
    - Formato B — Áudio: gravação de 1 min no app nativo do sistema (gratuito, sem instalação).
    - Formato C — Desenho anotado: ilustração do planeta com legendas curtas escritas à mão.
  - **Materiais:** Computadores com Google Docs (TTS nativo gratuito), app de gravação nativo, folhas de desenho.
  - **Critério de Avaliação:** O registro (em qualquer formato) inclui ao menos 2 características científicas corretas do planeta escolhido. A avaliação incide sobre o conteúdo — o formato não é critério de nota.
 
---
"""
}


# 4. FUNÇÕES DE GERAÇÃO (2 MODOS PARA O EXPERIMENTO COMPARATIVO)
def LLM_Setup(prompt_text):
    chave = os.getenv("GOOGLE_API_KEY")
    
    model = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash-001",
        google_api_key=chave,
        temperature=0.0
    )
    parser = StrOutputParser()
    chain = model | parser
    return chain.invoke(prompt_text)


def selecionar_exemplos_icl(perfis_selecionados: list) -> str:
    """
    Seleciona dinamicamente os exemplos few-shot pelos perfis escolhidos.
    Se múltiplos perfis forem selecionados, injeta também o exemplo
    'Múltiplos Perfis' para guiar o modelo no caso de coexistência.
    """
    if not perfis_selecionados:
        return Banco_de_exemplos["TDAH"]

    exemplos = [Banco_de_exemplos[p]
                for p in perfis_selecionados if p in Banco_de_exemplos]

    # Injeta o exemplo de múltiplos perfis quando há mais de um perfil
    # para ensinar o modelo a lidar com coexistência de necessidades
    if len(perfis_selecionados) > 1 and "Múltiplos Perfis" not in perfis_selecionados:
        exemplos.append(Banco_de_exemplos["Múltiplos Perfis"])

    return "\n".join(exemplos)


def gerar_prompt_simples(subject, topic, grade, duration, objectives, bncc, perfis_str):
    """
    MODO 2 — Prompt Estruturado Simples:
    Menciona o DUA e seus três princípios, mas sem exemplos few-shot.
    Representa prompt engineering tradicional.
    """
    return LLM_Setup(f"""
Você é um especialista em Educação Inclusiva e Desenho Universal para a Aprendizagem (DUA).
Sua tarefa é gerar planos de aula que eliminem barreiras de aprendizagem seguindo RIGOROSAMENTE
a estrutura dos três princípios do DUA (CAST, 2018):
1. Múltiplos Meios de Engajamento
2. Múltiplos Meios de Representação
3. Múltiplos Meios de Ação e Expressão

Dados:
- Disciplina: {subject} | Tópico: {topic} | Habilidade BNCC: {bncc}
- Série: {grade} | Duração: {duration} minutos
- Perfis de Inclusão: {perfis_str}
- Objetivos: {objectives}

**SAÍDA ESPERADA (Plano DUA):**
Inclua obrigatoriamente:
1. Nome do Plano, Ano de Ensino e Habilidades BNCC
2. Proposta de Dinâmica com critério de agrupamento e gestão do tempo
3. Três atividades (Foco 1 / Foco 2 / Foco 3) cada uma com Descrição, Acessibilidade e Critério de Avaliação

Adapte cada seção especificamente para os perfis informados.
Responda em Markdown formatado.
""")


def gerar_icl(subject, topic, grade, duration, objectives, bncc, perfis_str, perfis_lista):
    """
    MODO 2 — ICL Estático (contribuição principal do TCC):
    Injeta exemplos few-shot fixos selecionados pelo perfil da turma.
    Quando múltiplos perfis são selecionados, injeta também o
    exemplo 'Múltiplos Perfis' para guiar a coexistência de adaptações.
    """
    exemplos = selecionar_exemplos_icl(perfis_lista)
    prompt = f"""
Você é um especialista em Educação Inclusiva e Desenho Universal para a Aprendizagem (DUA).
Sua tarefa é gerar planos de aula que eliminem barreiras de aprendizagem seguindo RIGOROSAMENTE
a estrutura dos três princípios do DUA (CAST, 2018):
1. Múltiplos Meios de Engajamento
2. Múltiplos Meios de Representação
3. Múltiplos Meios de Ação e Expressão

{"="*60}
EXEMPLOS DE REFERÊNCIA (few-shot):
{"="*60}

{exemplos}

{"="*60}
AGORA GERE O PLANO PARA O SEGUINTE CASO:
{"="*60}

**ENTRADA:**
- Disciplina: {subject} | Tópico: {topic} | Habilidade BNCC: {bncc}
- Série/Ano: {grade} | Duração: {duration} minutos
- Perfis de Inclusão: {perfis_str}
- Objetivos de Aprendizagem: {objectives}

**SAÍDA ESPERADA (Plano DUA):**
Inclua obrigatoriamente:
1. Nome do Plano, Ano de Ensino e Habilidades BNCC
2. Proposta de Dinâmica com critério de agrupamento e gestão do tempo
3. Três atividades (Foco 1 / Foco 2 / Foco 3) cada uma com Descrição, Acessibilidade e Critério de Avaliação

Adapte cada seção especificamente para os perfis informados.
Responda em Markdown formatado.
"""
    return LLM_Setup(prompt), exemplos


# 5. EXPORTAÇÃO PDF

def export_to_pdf(conteudos: dict, subject, topic):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    for modo, conteudo in conteudos.items():
        pdf.add_page()
        pdf.set_font("Helvetica", style='B', size=14)
        modo_clean = modo.encode('ascii', 'replace').decode('ascii')
        pdf.cell(0, 10, txt=f"Plano DUA - {modo_clean}", ln=True, align='C')
        pdf.set_font("Helvetica", size=10)
        subject_clean = subject.encode('ascii', 'replace').decode('ascii')
        topic_clean = topic.encode('ascii', 'replace').decode('ascii')
        pdf.cell(
            0, 8, txt=f"Disciplina: {subject_clean} | Topico: {topic_clean}", ln=True)
        pdf.ln(3)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(4)
        pdf.set_font("Helvetica", size=10)
        clean = conteudo.encode('ascii', 'replace').decode('ascii')
        pdf.multi_cell(0, 7, txt=clean)

    return bytes(pdf.output())


# 6. INTERFACE STREAMLIT — TRÊS ABAS
st.title('🎓 Inclua: Planejador Inclusivo')
st.markdown("""
Ferramenta de pesquisa para geração de planos de aula inclusivos com  
**In-Context Learning Estático** alinhado ao **Desenho Universal para a Aprendizagem (DUA)**.
""")

aba_gerador, aba_comparativo = st.tabs([
    "📝 Gerador de Planos",
    "🔬 Experimento Comparativo",
])


# ABA 1 — GERADOR PRINCIPAL (modo ICL)

with aba_gerador:
    st.subheader("Gerador com ICL Estático")

    col1, col2 = st.columns(2)
    with col1:
        subject_input = st.text_input(
            'Disciplina', placeholder="Ex: Computação", key="g_sub")
        grade_input = st.text_input(
            'Ano/Série', placeholder="Ex: 1º Ano Ensino Médio", key="g_grade")
        bncc_input = st.text_input(
            'Habilidade BNCC', placeholder="Ex: (EF01LP05)", key="g_bncc")
    with col2:
        topic_input = st.text_input(
            'Tópico da Aula', placeholder="Ex: Algoritmos", key="g_topic")
        duration_input = st.text_input(
            'Duração (min)', placeholder="Ex: 50", key="g_dur")

    perfil_turma = st.multiselect(
        "Perfis de Inclusão na Turma",
        [k for k in Banco_de_exemplos.keys() if k != "Múltiplos Perfis"],
        help="Exemplos few-shot serão selecionados dinamicamente. Ao selecionar mais de um perfil, o exemplo 'Múltiplos Perfis' é injetado automaticamente."
    )

    objectives_input = st.text_area(
        'Objetivos de Aprendizagem',
        placeholder="O que os alunos devem ser capazes de fazer ao final da aula?",
        key="g_obj"
    )

    if st.button('Gerar Plano de Aula (ICL)', type="primary"):
        if not all([subject_input, topic_input, grade_input, duration_input, objectives_input, bncc_input]):
            st.warning('Preencha todos os campos obrigatórios.')
        else:
            with st.spinner('Selecionando exemplos ICL e gerando plano DUA...'):
                try:
                    perfis_str = ', '.join(
                        perfil_turma) if perfil_turma else "Turma geral"
                    output, exemplos_usados = gerar_icl(
                        subject_input, topic_input, grade_input,
                        duration_input, objectives_input, bncc_input,
                        perfis_str, perfil_turma
                    )
                    with st.expander("🔍 Exemplos ICL estáticos injetados no prompt (transparência acadêmica)"):
                        st.markdown(exemplos_usados)
                    st.divider()
                    st.markdown(output)
                    pdf_bytes = export_to_pdf(
                        {"ICL Estatico": output}, subject_input, topic_input)
                    st.download_button(
                        label="📥 Baixar Plano em PDF",
                        data=pdf_bytes,
                        file_name=f"Plano_DUA_ICL_{topic_input.replace(' ', '_')}.pdf",
                        mime="application/pdf"
                    )
                except Exception as e:
                    st.error(f"Erro: {e}")


# ABA 2 — EXPERIMENTO COMPARATIVO (coração do TCC)

with aba_comparativo:
    st.subheader("🔬 Experimento Comparativo")
    st.info("""
   ** Esta aba gera o mesmo plano pelos dois modos em paralelo.
    """)

    col1, col2 = st.columns(2)
    with col1:
        c_subject = st.text_input(
            'Disciplina', placeholder="Ex: Biologia", key="c_sub")
        c_grade = st.text_input(
            'Ano/Série', placeholder="Ex: 2º Ano EM", key="c_grade")
        c_bncc = st.text_input(
            'Habilidade BNCC', placeholder="Ex: (EF09CI08)", key="c_bncc")
    with col2:
        c_topic = st.text_input(
            'Tópico da Aula', placeholder="Ex: Célula", key="c_topic")
        c_duration = st.text_input(
            'Duração (min)', placeholder="Ex: 50", key="c_dur")

    c_perfis = st.multiselect(
        "Perfis de Inclusão",
        [k for k in Banco_de_exemplos.keys() if k != "Múltiplos Perfis"],
        key="c_perfis"
    )

    c_objectives = st.text_area(
        'Objetivos de Aprendizagem',
        placeholder="O que os alunos devem ser capazes de fazer ao final da aula?",
        key="c_obj"
    )

    if st.button('▶ Executar Experimento Comparativo', type="primary"):
        if not all([c_subject, c_topic, c_grade, c_duration, c_objectives, c_bncc]):
            st.warning('Preencha todos os campos.')
        else:
            perfis_str = ', '.join(c_perfis) if c_perfis else "Turma geral"
            col_p, col_i = st.columns(2)

            with col_p:
                with st.spinner('Gerando Prompt Estruturado...'):
                    try:
                        out_prompt = gerar_prompt_simples(
                            c_subject, c_topic, c_grade, c_duration,
                            c_objectives, c_bncc, perfis_str)
                        st.markdown("#### Modo 1 — Prompt Estruturado")
                        st.caption("DUA mencionado, sem exemplos few-shot.")
                        st.markdown(out_prompt)
                        st.session_state['prompt_simples'] = out_prompt
                    except Exception as e:
                        st.error(f"Erro Prompt Estruturado: {e}")

            with col_i:
                with st.spinner('Gerando ICL Estático...'):
                    try:
                        out_icl, exemplos_usados = gerar_icl(
                            c_subject, c_topic, c_grade, c_duration,
                            c_objectives, c_bncc, perfis_str, c_perfis)
                        st.markdown("#### Modo 2 — ICL Estático ⭐")
                        st.caption(
                            "Exemplos fixos selecionados pelo perfil da turma.")
                        with st.expander("Ver exemplos ICL injetados"):
                            st.markdown(exemplos_usados)
                        st.markdown(out_icl)
                        st.session_state['icl'] = out_icl
                    except Exception as e:
                        st.error(f"Erro ICL Estático: {e}")

            if all(k in st.session_state for k in ['prompt_simples', 'icl']):
                st.divider()
                pdf_comp = export_to_pdf({
                    "Modo 1 — Prompt Estruturado": st.session_state['prompt_simples'],
                    "Modo 2 — ICL Estatico": st.session_state['icl']
                }, c_subject, c_topic)

                st.download_button(
                    label="📥 Baixar Comparativo Completo em PDF",
                    data=pdf_comp,
                    file_name=f"Comparativo_DUA_{c_topic.replace(' ', '_')}.pdf",
                    mime="application/pdf"
                )
