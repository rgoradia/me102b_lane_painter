% get binary 
clear all 
clc 
filepath = 'lines.png';
im = imread(filepath) ; 
fileID = fopen('lines.txt','w') ; 
shape = size(im) ;

for i = 1: shape(1)
    for j = 1:shape(2)
        if im(i,j,1)~= 0 && im(i,j,1)~=2
            mat(i,j) = 0 ;
        else 
            mat(i,j) = 1 ; 
        end 
    end 
end 
imshow(mat) 

%% 
for j = 1:shape(1)
fprintf(fileID,'%d',mat(j,:));
fprintf(fileID, '\n') ;
end 
fclose(fileID) ; 