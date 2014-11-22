from bottle import route, run, static_file


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./webpageFiles')

run(host='0.0.0.0', port=8080, debug=True, reloader=True)