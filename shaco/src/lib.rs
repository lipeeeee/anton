use pyo3::prelude::*;

/// Sample Async code
#[pyfunction]
fn rust_sleep(py: Python<'_>) -> PyResult<&PyAny> {
    pyo3_asyncio::tokio::future_into_py(py, async {
        tokio::time::sleep(std::time::Duration::from_secs(2)).await;
        println!("Hello depois de 2sec");
        Ok(Python::with_gil(|py| py.None()))
    })
}

/// Queries windows process manager to know if league is open
#[pyfunction]
fn is_league_open() -> PyResult<bool> {
    
    Ok(true)
}

/// Starts League of Legends in an offline state
#[pyfunction]
fn start_league_offline(py: Python<'_>) -> PyResult<()> {
    // Check if the client is already running.

    // TODO: Implement the logic to check if the client is running.

    // Step 1: Open a port for our chat proxy.

    // Step 2: Find the Riot Client.

    // TODO: Implement the logic to find the Riot Client path.

    // Step 3: Start proxy web server for clientconfig.

    // TODO: Implement the logic to start the proxy web server.

    // Step 4: Launch Riot Client (+game).

    // TODO: Construct the command to launch the Riot Client with the appropriate arguments.

    // Step 5: Get chat server and port for this player by listening to event from ConfigProxy.

    // Step 6: Connect sockets.

    // Step 7: All sockets are now connected, start tray icon.

    // TODO: Implement the main logic of your program that handles incoming and outgoing connections.

    Ok(())
}

/// Shaco Module that takes care of masking league status
/// while providing other utility features
#[pymodule]
fn shaco(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(rust_sleep, m)?)?;
    
    // Shaco
    m.add_function(wrap_pyfunction!(is_league_open, m)?)?;
    m.add_function(wrap_pyfunction!(start_league_offline, m)?)?;

    Ok(())
}
