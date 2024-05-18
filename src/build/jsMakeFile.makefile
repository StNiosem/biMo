# js to C confverter
buildutils_configure{
	export $OUTLOCATION = "./build/artefact"
	export $DSTLOCATION = "./dist/pes"
	export $FA_LOCATION = "./dist"
}

build_bimo_starter{
	cd "./start"
	node-build --JS-to-C bimo.js --outfile='./build/artefact/start/bimo.elf'	
}

build_bimo_server{
	server.auth{
		cd "./server/auth"
		node-build --JS-to-C --filelist='./build/server/auth.txt' --outfile'./build/artefact/server/auth/*.elf'
	}
	server.database{
		cd "./server/database"
		node-build --JS-to-C --filelist='./build/server/database.txt' --outfile'./build/artefact/server/database/*.elf'
	}
}