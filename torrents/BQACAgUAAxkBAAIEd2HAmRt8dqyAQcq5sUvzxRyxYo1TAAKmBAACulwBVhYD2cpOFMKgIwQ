<?php
session_start();
include 'php/process.php';

$from = $_SESSION['id'];
$to = $_SESSION['to'];
$lastid =$_POST['lastmessageid'];

$messages=[];
connect_database();
$sql = "select * from chat where id>$lastid and ((user_from=$from and user_to=$to) or (user_from=$to and user_to=$from)) ";
$result = $conn->query($sql);


$id;
while ($row = $result->fetch_assoc()) {
    $messages[]=array("message"=>$row['message'],"from"=>$row['user_from'],"to"=>$row['user_to']);
    $id= $row['id'];
}


$messages[]=$id;

echo json_encode($messages);
