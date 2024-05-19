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

	server.push{
		cd "./server"
		node-build --JS-to-C --filelist='./build/server/push.txt' --outdir='./build/artefact/server/push'
	}

	server.auth{
		cd "./server/auth"
		node-build --JS-to-C --filelist='./build/server/auth.txt' --outdir='./build/artefact/server/auth'
	}

	server.database{
		cd "./server/database"
		node-build --JS-to-C --filelist='./build/server/database.txt' --outdir='./build/artefact/server/database'
	}
}

build_bimo_client{
	client.frontend{
		cd "./client/frontend"
	}
}