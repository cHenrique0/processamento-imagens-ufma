clear all
close all
clc

imgOrig = imread('kobi.png');
imgTest = imgOrig;

K = 4;
[Nr, Nc] = size(imgTest);
gamma = 1; b = 1; Theta = 0:pi/6:pi-pi/6; phi = 1; shape = 'valid';

% J. Zhang
J = (2.^(0:log2(Nc/8)) - .5) ./ Nc;
F = [ (.25 - J) (.25 + J) ]; F = sort(F); Lambda = 1 ./ F;
[seg,O] = GaborTextureSegment(imgTest, K, gamma, Lambda, b, Theta, phi, shape);
figure, imshow(uint8(seg*50))
