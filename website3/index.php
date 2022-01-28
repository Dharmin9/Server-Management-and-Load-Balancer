<!DOCTYPE html>
<html>
<body>
<h1>Current products on sale:</h1>
<?php

    $json = file_get_contents('http://product-api-service');
    $temp = json_decode($json, true);
    echo "<table border=1>";
    echo "<tr>";
    echo "<td style='font-weight: 700;'>name</td>";
    echo "<td style='font-weight: 700;'>quantity</td>";
    echo "<td style='font-weight: 700;'>price</td>";
    echo "</tr>";
        foreach ($temp["products"] as $product){
            echo "<tr>";  
            echo "<td>{$product['item']}</td>";
            echo "<td>{$product['qty']}</td>";
            echo "<td>{$product['price']}</td>";
            echo "</tr>";
            
        }
    
    echo "</table>";
?>
</body>
</html>