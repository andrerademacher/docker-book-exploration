<?php

declare(strict_types=1);

$date = date('c');
$load = sys_getloadavg()[0] ?: 'not available';
require_once __DIR__ . '/template.php';