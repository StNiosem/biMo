function ServerConnector(serverAddress, modelAddr, path) {
    path = SrcLookup.Server(serverAddress);
    SrcLookup.Connect(path);
    ModelLookup.Lookup.Server(modelAddr, path)   
    
    function SignFile(filePath, certPath, privateKey) {
        certAttach(filePath, certPath);
        privSign(certPath, privateKey);
        filePrivate(filePath, privateKey);
    }
}