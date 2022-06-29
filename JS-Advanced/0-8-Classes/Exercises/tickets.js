function solve(data, criteria) {
    class Ticket {
        constructor(destination, price, status) {
            this.destination = destination;
            this.price = price;
            this.status = status;
        }
    }

    function sortByCriteria(tickets) {
        const possibleSortingCriteria = {
            'destination': () => tickets.sort((a, b) => a.destination.localeCompare(b.destination)),
            'price': () => tickets.sort((a, b) => a.price - b.price),
            'status': () => tickets.sort((a, b) => a.status.localeCompare(b.status)),
        };

        return possibleSortingCriteria[criteria]();
    }

    const message = [];

    for (const line of data) {
        let [destination, price, status] = line.split('|');
        price = Number(price);
        message.push(new Ticket(destination, price, status));
    }

    return sortByCriteria(message);
}


console.log(solve(['Philadelphia|94.20|available',
        'New York City|95.99|available',
        'New York City|95.99|sold',
        'Boston|126.20|departed'],
    'destination'));
