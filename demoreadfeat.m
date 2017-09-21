

name = '--DwgB78t-c';

trainval = 'train-feat/';
featfile = strcat(trainval ,name, '.feat.bin')

fileID = fopen(featfile);
feat = fread(fileID,  'float')