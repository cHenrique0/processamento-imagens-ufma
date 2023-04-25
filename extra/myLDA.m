% LDA - Luis Claudio

clc
clear all

X = [ 2.95 6.63; % classe 1
2.53 7.79;       % classe 1
3.57 5.65;       % classe 1
3.16 5.47;       % classe 1
2.58 4.46;       % classe 2
2.16 6.22;       % classe 2
3.27 3.52 ];     % classe 2 

m1 = mean(X(1:4,:));
m2 = mean(X(5:7,:));
m = mean(X);

S1 = (X(1:4,:) - repmat(m1,4,1))' * (X(1:4,:) - repmat(m1,4,1));
S2 = (X(5:7,:) - repmat(m2,3,1))' * (X(5:7,:) - repmat(m2,3,1));

Sw = S1 + S2; % Sw

w=inv(Sw)*(m1-m2)'; % (Sw)^-1 * Sb
w = w/norm(w);

figure, hold on
plot(X(1:4,1),X(1:4,2),'bx');
plot(m1(1),m1(2),'bd');
plot(X(5:7,1),X(5:7,2),'rx');
plot(m2(1),m2(2),'rd');
plot(m(1),m(2),'kd');

X1proj=(X(1:4,:)*w)*w';
X2proj=(X(5:7,:)*w)*w';

figure, hold on
plot(X1proj(:,1),X1proj(:,2),'bo');
plot(X2proj(:,1),X2proj(:,2),'ro');

% Teste
teste = [3 5];
testeproj = (teste*w)*w';
hold on
plot(testeproj(:,1),testeproj(:,2),'go');

% Medida de corte
projX = (X*w)*w';
corte = mean(projX);

hold on
plot(corte(1),corte(2),'k*');
if mean(testeproj < corte) == 1
    disp('classe 1')
else
    disp('classe 2')
end