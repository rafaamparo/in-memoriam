# in-memoriam
Jogo feito como trabalho final da disciplina de Laboratório de Programação de Jogos na Universidade Federal Fluminense.


![Screenshot of the final battle](https://github.com/rafaamparo/in-memoriam/assets/101950734/aad80bed-2838-42ec-b802-c1b891272538)

O jogo parte da premissa de um shooter game top-down que consiste, basicamente, em lutar contra hordas de zumbis que crescem progressivamente a cada round - e, a cada 5 rodadas, é oferecida a chance de lutar contra um boss. Durante a dinâmica da transição de rodadas, são oferecidas algumas melhorias cumulativas para o player na(s) rodada(s) seguinte(s). Esteticamente, todo o projeto mantém-se fiel à estética arcade 8-bit, dos visuais à trilha sonora. O jogo foi desenvolvido por meio do framework Pygame e modularizado em diversas classes e funções.

**O que um dia foi seu mundo, agora é uma terra devastada. Já fazem décadas desde que Lorde Gargo e sua tropa de zumbis dizimaram o planeta - e você perdeu suas duas irmãs na guerra. O santuário mágico e as memórias de onde você e sua família um dia foram felizes é tudo que te resta em tantos anos de solidão... mas eles te encontraram. Prepare-se para lutar. Por tudo que tiraram de você!**
<sub>_(Sinopse presente na tela de menu do jogo.)_</sub>

_Mecânicas implementadas:_

- Moedas e Upgrade System: a cada rodada, o jogador recebe a opção de pagar por upgrades que trazem vantagens ao seu jogo. A duração de cada upgrade varia entre um a dois rounds e eles podem ser cumulativos - um jogador pode até mesmo comprar as quatro opções oferecidas e usá-las enquanto sua duração não expirar. As moedas possuem uma lógica simples: o jogador começa com 30 e, a cada zumbi morto, recebe mais 15.

- Zumbis: os zumbis, gerados em um for loop cujo range é dobrado a cada round até atingir a horda-limite de 200 inimigos, foram implementados seguindo uma lógica parecida com o algoritmo de Boids para evitar aglomeração entre eles, visto que, como todos seguem a protagonista a todo momento, era necessário´impedir que toda uma horda se concentrasse em um mesmo ponto. Os zumbis normalmente possuem duas vidas, representadas em uma barra de saúde, e, quando recebem o primeiro tiro dado pela personagem, são “jogados para trás” em um distância gerada de forma randômica entre 30-100 pixels.

- Controles e Tiros: o movimento do jogador é feito com o input das teclas WASD, podendo se mover nas 4 direções e suas respectivas diagonais. O jogador pode atirar com o teclado com a tecla SPACE, de forma tal que os tiros seguirão a direção W/A/S/D do momento ou com o mouse - nesses tiros, é encontrado e normalizado um vetor direção do tiro, e, com a função **math.atan2**, o ângulo cuja tangente é o quociente entre as coordenadas dadas.

- Armas: a protagonista possui um “cajado” mágico que é a fonte de seus disparos contra os zumbis.

- Sistema de Vidas: a protagonista inicia o jogo com 3 vidas, que são perdidas caso haja colisão com um zumbi ou, no caso da fase especial, com o boss. Enquanto as idas da protagonista são exibidas no canto da tela, os zumbis e o boss possuem uma barra de vida exibindo sua saúde e quanto já receberam de dano.

- Boss Round: a cada 5 rodadas, é oferecida ao player a opção de lutar contra o mestre dos zumbis, Lorde Gargo, caso pague 2000 moedas. O pagamento desbloqueará a possibilidade de escolher entre uma das “bênçãos” oferecidas pelas falecidas irmãs da protagonista: dano duplo contra o boss ou o ganho de 12 vidas na luta contra o inimigo, que é consideravelmente mais rápido que os zumbis e possui, por si só, 10 vidas.

- Câmera: a câmera com zoom implementada no jogo segue a protagonista pelo mapa e a usa como centro de referência, com um offset obtido na subtração das coordenadas do sprite com as medidas da tela.


