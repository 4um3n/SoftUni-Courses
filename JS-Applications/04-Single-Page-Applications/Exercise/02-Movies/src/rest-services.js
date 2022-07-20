export async function sendRequest(url, init) {
    try {
        const response = await fetch(url, init);
        const data = await response.json();

        if (response.status !== 200) {
            throw new Error(data.message)
        }

        return data
    } catch (error) {
        alert(error.message)
    }
}
