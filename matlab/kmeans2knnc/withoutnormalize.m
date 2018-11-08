%pick data 1 - 23 normal s ... 
K_start = k(:,[1:38]);
K = k(:,[1:38]);

for i = 1:23
    temp = num2str(i);
    eval(['a' temp '=K(find(k(:,39)==' temp '),:);'])
    eval(['[I,C' temp ']=kmeans(a' temp ',1);'])
end
Big=[]
for j = 1:100
    distance = [];
    for i = 1:23
        temp = num2str(i);
        temp2 = num2str(j);
        eval(['distance = [distance K(' temp2 ',:)*C' temp '''];'])
    end
    [a,b] = sort(distance);
    Big = [Big b(1)];
end
% [a,b] = sort(distance)  %diyige b(1) fenleibie
