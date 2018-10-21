# PDSB


Homework B - Processamento de Sinais Biomédicos
Q1 - Aplicar autocorrelação para detecção de sinais na presença de ruído:
  - x1 = senóide 1Vpp, 17Hz
  - x2 = ruído aleatório, 5Vpp
  - x(t) = x1(t) + x2(t)
  
Q2 - Calcular a convolução digital da seguinte sequência de dados x(t) com a resposta ao impulso do sistema h(t).
  - x(t) = exp(-0,5t);  0<=t <=32T, T=1
  - h(t) = [0 1,5 0,75 0,375 0,1875 0,09375 0,046875 0,0234375]
  -- Faça o gráfico de x(t), h(t), y(t)
  
Q3 - Mostre o gráfico da resposta de frequência do filtro FIR calculado em sala.
  - Gerar o Seguinte Sinal:
    - S = sin(2pif1)+sin(2pif2)+sin(2pif3)
      f1 = 750Hz
      f2 = 2500Hz
      f3 = 3250Hz
    - Calcule o espectro de frequência de S.
    - Filtre o sinal S utilizando o filtro projetado, mostrando a saída do filtro e o espectro de frequência do sinal filtrado.
    - Faça a superposição do dois espectros calculados acima.
    
Q4 - Usando o método da colocação de pólos e zeros no plano Z (Use o sinal de ECG de 1min @ 1000Hz, ECG_03).
  - Calcule os coeficientes do filtro notch.
  - Obtenha a função de transferência, a equação de diferenças e a representação em blocos para a seguinte especificação:
    - Notch Frequency 60Hz.
    - 3dB width of notch +- 5Hz
    - Sampling frequency 1200Hz ou alguma frequência múltipla de 60Hz
  - Filtre o sinal original do item (1) utilizando o filtro projetado e mostre os resultados
