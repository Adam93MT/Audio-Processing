function [ norm ] = normalize( A )
    norm = A/(max(abs(A)));
end

