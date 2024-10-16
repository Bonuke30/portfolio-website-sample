<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rank Table</title>
    <style>
        table {
            width: 50%;
            border-collapse: collapse;
            margin: 20 px 0;
            font-size: 18px;
            text-align: left;
            border-radius: 8px;
            overflow: hidden;
        }
        th, td {
            padding: 12px 20px;
            border: 1px solid #ddd;
        }        th {
            background-color: #2AB07A;
            color: white;
            text-align: left;
        }
        td {
            font-weight: normal;
            text-align: left;
        }
        tr:nth-child(2) td:nth-child(2) {
            font-weight: bold;
            color: #2AB07A;
        }
        tr:nth-child(2) td:nth-child(4) {
            font-weight: bold;
            color: #2AB07A;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
    </style>
</head>
<body>

    <table>
        <thead>
            <tr>
                <th>Rank</th>
                <th>Name</th>
                <th>Points</th>
                <th>Team</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td>Domenic</td>
                <td>88,110</td>
                <td>dcode</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Sally</td>
                <td>72,400</td>
                <td>Students</td>
            </tr>
            <tr>
                <td>3</td>
                <td>Nick</td>
                <td>52,300</td>
                <td>dcode</td>
            </tr>
        </tbody>
    </table>

</body>
</html>
