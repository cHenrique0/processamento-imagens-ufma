% kmeans_light: K-means clustering using euclid distance. 
%
%  [dataCluster codebook] = kmeans_light(data, K, stopIter)
%
%  Input and output arguments ([]'s are optional):
%   data        (matrix) of size NxD. N is the number of data (classifiee) 
%                vectors,and D is the dimension of each vector. 
%   K           (scalar) The number of clusters. 
%   stopIter    (scalar) The threshold [0, 1] to stop learning iterations. 
%                Default is .05, and smaller makes continue interations.  
%   dataCluster (matrix) of size Nx1: integers indicating the cluster indicies.
%                dataCluster(i) is the cluster id for data item i. 
%   codebook    (matrix) of size KxD: set of cluster centroids, VQ codewords.
%
% See also: autolabel.m
%
% Author : Naotoshi Seo
% Date   : April, 2006
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function [dataCluster ,codebook] = kmeans_light(data, K, stopIter)
 if nargin < 3,
     stopIter = .01;
 end
 [N dim] = size(data);
 if K > N,
     error('K must be less than or equal to the # of data');
 end

 % Initial codebook
 codebook = data(randsample(N, K), :);

 improvedRatio = Inf;
 distortion = Inf;
 iter = 0;
 while true 
     % Calculate euclidean distances between each sample and each codeword
     d = eucdist2(data, codebook);
     % Assign each sample to the nearest codeword (centroid)
     [dataNearClusterDist, dataCluster] = min(d, [], 2);
     % distortion. If centroids are unchanged, distortion is also unchanged.
     % smaller distortion is better
     old_distortion = distortion;
     distortion = mean(dataNearClusterDist);
     
     % If no more improved, break;
     improvedRatio = 1 - (distortion / old_distortion);
     % fprintf('%d: improved ratio = %f\n', iter, improvedRatio); iter = iter + 1; 
     if improvedRatio <= stopIter, break, end;
     
     % Renew codebook
     for i=1:K
         % Get the id of samples which were clusterd into cluster i.
         idx = find(dataCluster == i);
         % Calculate centroid of each cluter, and replace codebook
         codebook(i, :) = mean(data(idx, :));
     end 
 end

%%%% Euclidean distance matrix between row vectors in X and Y %%%%%%%
%  Input and output arguments 
%   X: NxDim matrix
%   Y: PxDim matrix
%   d: distance matrix of size NxP 
function d=eucdist2(X,Y);
 U=~isnan(Y); Y(~U)=0;
 V=~isnan(X); X(~V)=0;
 d=abs(X.^2*U'+V*Y'.^2-2*X*Y');
