%filename= strcat(dir, 'test.e');
args = argv();
obj = NicoletFile(args{1});
b = obj.segments.samplingRate

n = obj.segments.chName;

infos = obj.segments

startDate = infos.startDate
startTime = infos.startTime

disp(startTime)
disp(startDate)
disp(infos)

tmpFolder = "tmp/"
for i = 1:1000
    disp(["Segment " num2str(i)])
    len = obj.getNrSamples(i);
    disp(["# of channels: " num2str(size(len)(2))])
    for channel = 1:size(len)(2)
        disp(["Channel '" n{1,channel} "': " num2str(channel) " of segment " num2str(i)])
        disp(["Num of samples: " num2str(len(channel))])
        disp(["Sampling rate: " num2str(b(channel))])
        fname = [num2str(i) "." num2str(channel) " - " n{1,channel} " @" num2str(b(channel)) "Hz.csv"]
        a = obj.getdata(i, [1 len(channel)], channel:channel);
        dlmwrite (strcat(tmpFolder,fname), a, ",")
        disp([ "Channel file written: " strcat(tmpFolder,fname)])
    endfor
endfor

%a = obj.getdata(1, [1 115000], 1:9);
%b = (obj.segments.samplingRate)
%disp(b)

%disp(a)


%dlmwrite ("out.csv", a', ",")