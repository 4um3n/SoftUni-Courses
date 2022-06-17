function solve(area, vol, data) {
    return JSON.parse(data).map(obj => ({
        'area': area.call(obj),
        'volume': vol.call(obj)
    }));
}
