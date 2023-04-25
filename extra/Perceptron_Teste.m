clear all
clc

% Implementação da porta AND
P = [0 0 1 1; 0 1 0 1];  % Entrada
T = [0 0 0 1];           % Saida

w = [1 1]; % Pesos iniciais
b = 1; % Bias inicial
epoc = 5; % Variar conforme a precisao

% Treinamento
for j = 1:epoc
    for i = 1:size(P,2)
        p = P(:,i);
        t = T(i);
        [w b] = perceptron(p',t,w,b);
        fprintf('Epoca: %d, w1: %d, w2: %d, bias: bias: %d\n',j,w,b);
    end
end

disp('Teste:')
teste = [0 0]'; % Entrada
saida = w*teste + b; % Obtem saida na rede treinada
if saida<0.5
    disp('0')
else
    disp('1')
end