function [W_new, b_new] = perceptron(P,t,W,b)
    a = 1/(1+exp(-(W*P'+b))); % Saída da rede na função de ativação
    e = t - a; % Erro (desejado - valor_atual)
    W_new = W + e.*P; % Atualiza os pesos
    b_new = b + e; % Atualiza o bias
end