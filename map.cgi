#!/usr/bin/perl -wT
use strict;
use CGI qw(:cgi); #use CGI
use CGI::Carp qw(fatalsToBrowser); # Send error messages to browser

# Take value from post method
my $input = param("gene_name");

# Define environment pathway
$ENV{'PATH'} = '/bin:/usr/bin';

# http://www.broadinstitute.org/igv/projects/current/igv.php?sessionURL=localhost/accepted_hits.bam&genome=rn6&locus=$locus

# Generate HTML template of IGV browser.
print <<END_OF_HTML;
Content-type: text/html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="//igv.org/web/img/favicon.ico">
    <title>Integrative Genomics Viewer - BAM Example</title>

    <!-- Bootstrap CSS - for demo only, NOT REQUIRED FOR IGV -->
    <link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">

    <!-- jQuery UI CSS -->
    <link rel="stylesheet" type="text/css"
          href="//ajax.googleapis.com/ajax/libs/jqueryui/1.11.2/themes/smoothness/jquery-ui.css"/>

    <!-- Font Awesome CSS -->
    <link rel="stylesheet" type="text/css"
          href="//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css"/>

    <!-- IGV CSS -->
    <link rel="stylesheet" type="text/css" href="//igv.org/web/release/1.0.1/igv-1.0.1.css">

    <!-- bam.css n - for demo only, NOT REQUIRED FOR IGV -->
    <link rel="stylesheet" type="text/css" href="http://igv.org/web/examples/css/bam.css">

    <!-- jQuery JS -->
    <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jqueryui/1.11.2/jquery-ui.min.js"></script>

    <!-- Bootstrap JS - for demo only, NOT REQUIRED FOR IGV -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>

    <!-- IGV JS-->
    <script type="text/javascript" src="//igv.org/web/release/1.0.1/igv-1.0.1.js"></script>


</head>

<body>

<div class="jumbotron">

    <div class="container">
        <h2>IGV.js embedded in a Bootstrap page opened on a BAM file.</h2>
    </div>
    <!-- container -->

</div>
<!-- jumbotron -->

<div class="container-fluid" id="igvDiv" style="padding:5px; border:1px solid lightgray"></div>


<script type="text/javascript">

    $(document).ready(function () {

        var div = $("#igvDiv")[0],
                options = {
                    showNavigation: true,
                    showRuler: true,
                    genome: "hg19",
                    locus: "chr12:98,997,292-98,997,392",
                    tracks: [
                        {
                            name: "Genes",
                            url: "//s3.amazonaws.com/igv.broadinstitute.org/annotations/hg19/genes/gencode.v18.collapsed.bed",
                            displayMode: "EXPANDED"

                        },                        {
                            url: 'https://data.broadinstitute.org/igvdata/BodyMap/hg19/IlluminaHiSeq2000_BodySites/brain_merged/accepted_hits.bam',
                            name: 'Brain (BodyMap)'
                        }

                    ]
                };

        igv.createBrowser(div, options);

    });

</script>

</body>

</html>

END_OF_HTML

