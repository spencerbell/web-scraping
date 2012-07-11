<?xml version="1.0"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="text" encoding="iso-8859-1"/>


<xsl:template match="/">
      <xsl:text>location_id&#x9;address&#x9;city&#x9;state&#x9;zip&#x9;phone&#xa;</xsl:text>
      <xsl:for-each select='//div[@class="column"]//ul//li//a'>
	      <xsl:value-of select="."/><xsl:text>&#x9;</xsl:text>
	      <xsl:text>&#xa;</xsl:text>
      </xsl:for-each>
</xsl:template>
</xsl:stylesheet> 
