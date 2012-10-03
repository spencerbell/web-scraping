<?php

/**
 * Description of AbstractScraper
 *
 * @author sherazsharif
 */
class AbstractScraper {

    public function __construct($services = null) {

        # Dependency injection
        foreach($services as $key => $value) {
            $this->$key = $value;
        }
    }


}

?>
