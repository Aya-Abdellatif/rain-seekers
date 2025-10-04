
weatherArray = JSON.parse(localStorage.getItem("data"));
function summarizeClothing(weatherArray) {
    const tempKArray = weatherArray.map(day => day.T2M);

    // Get min and max temperatures
    const minTemp = Math.min(...tempKArray);
    const maxTemp = Math.max(...tempKArray);

    // Define clothing categories based on temperature
    function tempToClothes(tempK) {
        if (tempK < 283.15) return "heavy/normal clothes";
        if (tempK < 293.15) return "normal clothes";
        return "light clothes";
    }

    // Find ranges where clothing is similar
    let summaries = [];
    let startIndex = 0;
    let currentClothes = tempToClothes(tempKArray[0]);

    for (let i = 1; i < tempKArray.length; i++) {
        const clothes = tempToClothes(tempKArray[i]);
        if (clothes !== currentClothes) {
            summaries.push({
                from: startIndex + 1,
                to: i,
                recommendation: currentClothes
            });
            startIndex = i;
            currentClothes = clothes;
        }
    }

    // Add the last range
    summaries.push({
        from: startIndex + 1,
        to: tempKArray.length,
        recommendation: currentClothes
    });

    return summaries;
}

const clothingSummary = summarizeClothing(weatherArray);
const summaryDiv = document.getElementById("clothing-summary");
