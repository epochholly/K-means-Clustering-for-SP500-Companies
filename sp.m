%% ============================
clear all; close all; clc;
[data,symbols,raw] = xlsread('sp500_short_period.xlsx','sp500');
movement = double((data(2:end,:)-data(1:end-1,:))>0)';
[m,n] = size(movement);
%% =============================
K = 10; % 10 sectors
max_iters = 1000;
rng(1209)
[idx,centroids] = km(movement,K,max_iters);
%% =============================
for i=1:K
    fprintf('\nStocks in group %d moving up together\n',i);
    char(symbols(idx == i))
end

