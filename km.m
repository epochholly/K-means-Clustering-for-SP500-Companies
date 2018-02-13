function [idx,centroids] = km(X,K,max_iters)

[m n] = size(X);
centroids = rand(K,n);
idx = zeros(m,1);
old_idx = zeros(m,1);

% Start looping
for j=1:max_iters
    change = false;
    for i=1:m
        [minval,idx(i)] = min(sum((repmat(X(i,:),K,1)-centroids).^2,2));
        if ((idx(i)~=old_idx(i)) && (change == false))
            change = true;
        end
    end
    for i=1:K
       centroids(i,:) = mean(X(idx==i,:),1); 
    end
    
    %if no more changing groups 
    if (change == false)  
       break;
    end

    old_idx = idx;

end

