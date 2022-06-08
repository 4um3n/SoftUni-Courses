function attachEventsListeners() {
    const fromUnitToMeters = {
        'km': n => n * 1000,
        'm': n => n,
        'cm': n => n * 0.01,
        'mm': n => n * 0.001,
        'mi': n => n * 1609.34,
        'yrd': n => n * 0.9144,
        'ft': n => n * 0.3048,
        'in': n => n * 0.0254
    };
    const fromMetersToUnit = {
        'km': n => n / 1000,
        'm': n => n,
        'cm': n => n / 0.01,
        'mm': n => n / 0.001,
        'mi': n => n / 1609.34,
        'yrd': n => n / 0.9144,
        'ft': n => n / 0.3048,
        'in': n => n / 0.0254
    };

    function convert(event) {
        let n = Number(document.getElementById('inputDistance').value);
        n = fromUnitToMeters[document.getElementById('inputUnits').value](n);
        document.getElementById('outputDistance').value =
            fromMetersToUnit[document.getElementById('outputUnits').value](n);
    }

    document.getElementById('convert').addEventListener('click', convert);
}
