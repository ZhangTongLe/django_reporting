def waveform(request):
    csv_file = 'your file'
    data = pd.read_csv(csv_file)
    TOOLS = "hover,crosshair,pan,wheel_zoom,box_zoom,reset,save,box_select"
    picture = figure(width=1200, height=400, tools=TOOLS)
    picture.line(data['order'], data['value'], color='blue', alpha=0.5)
    script, div = components(picture, CDN)
    return render(request, 'waveform.html', {'script': script, 'div': div})
