export async function fetchData(url) {
    const response = await fetch(
        "http://127.0.0.1:8000/"+url,
        {
            credentials: "include",
        }
    ); // Replace with your API endpoint URL
    if (!response.ok) {
        throw new Error("Failed to fetch data from the API");
    }
    const data = await response.json();
    return data;
}
