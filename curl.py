path = "../"
filename = "curl_raw.txt"
filename = path + filename

def reformat_curl(filename, inputs = None):
    with open(filename) as f:
        lines = f.readlines()
        line0 = lines[0].split('\\')[0]
        line1 = '-H ' + lines[1].split('\\')[0][9:]
        line2 = '-H ' + lines[2].split('\\')[0][9:][:-1]
        nshots = lines[4].split(":")[1].strip(" ")[:-1]
        params = {"num_shots": nshots}
        if inputs != None:
            params["inputs"] = inputs
        line3 = " --data '" + str(params) + "'"
    newcurl = line0 + line1 + line2 + line3
    print(newcurl)
    return newcurl

reformat_curl(filename)