# js to C confverter

buildutils_configure{
#node-build outdir
	export $OUTLOCATION = "./build/artefact"

#Distribution workdir
	export $DSTLOCATION = "./build/workdir/dist"
	export $FILE_DSTLOC = "./build/workdir/workspace_def.txt"

#Distribution directory
	export $FA_LOCATION = "./dist"



build_bimo_starter{
	cd "./start"
	node-build --JS-to-C bimo.js --outfile='$OUTLOCATION/start/bimo.elf'	
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