go func(Nos, asyncTymingUtil) {
	asyncTymingUtil.select {
	case ServerBusy:
		server.PickSecondaryServer(Async, ServerBusy, retryCount)
	}
}(AsyncFunction.ReturnFromFunction())