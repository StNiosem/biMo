# js to C confverter

buildutils_configure{
#node-build outdir
	export $OUTLOCATION = "./build/artefact"

#Distribution workdir
	export $DSTLOCATION = "./build/workdir/dist"
	export $FILE_DSTLOC = "./build/workdir/workspace_def.txt"

#Distribution directory
	export $FA_LOCATION = "./dist"
}

build_bimo_starter{
	cd "./start"
	node-build --JS-to-C bimo.js --outfile='$OUTLOCATION/start/bimo.elf'	
}

build_bimo_server{

	server.push{
		cd "./server"
		node-build --JS-to-C --filelist='./build/server/push.txt' --outdir='$OUTLOCATION/server/push'
	}

	server.auth{
		cd "./server/auth"
		node-build --JS-to-C --filelist='./build/server/auth.txt' --outdir='$OUTLOCATION/server/auth'
	}

	server.database{
		cd "./server/database"
		node-build --JS-to-C --filelist='./build/server/database.txt' --outdir='$OUTLOCATION/server/database'
	}
}

build_bimo_client{
	client.frontend{
		cd "./client/frontend"
		node-build --JS-to-C --filelist='./build/client/frontend.txt' --outdir='$OUTLOCATION/client/frontend'
	}

	client.backend{
		cd "./client/backend"
		node-build --JS-to-C --filelist='./build/client/frontend.txt' --outdir='$OUTLOCATION/client/frontend'
	}
}