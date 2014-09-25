'use strict';

angular.module('myApp.d3graph', ['ngRoute', 'd3'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/d3', {
            templateUrl: 'd3graph/d3graph.html',
            controller: 'd3graphCtrl'
        });
    }])

    .directive('barChart', ['d3Service', function (d3Service) {
        return {
            link: function (scope, element, attrs) {
                d3Service.d3().then(function (d3) {
                    // d3 is the raw d3 object
                });
            }}
    }])

    .directive('d3Bars', ['d3Service', function (d3Service) {
        return {
            restrict: 'EA',
            scope: {},
            link: function (scope, element, attrs) {
                d3Service.d3().then(function (d3) {
                    var svg = d3.select(ele[0])
                        .append('svg')
                        .style('width', '100%');

                    // Browser onresize event
                    window.onresize = function () {
                        scope.$apply();
                    };

                    // hard-code data
                    scope.data = [
                        {name: "Greg", score: 98},
                        {name: "Ari", score: 96},
                        {name: 'Q', score: 75},
                        {name: "Loser", score: 48}
                    ];

                    // Watch for resize event
                    scope.$watch(function () {
                        return angular.element($window)[0].innerWidth;
                    }, function () {
                        scope.render(scope.data);
                    });

                    scope.render = function (data) {
                        // remove all previous items before render
                        svg.selectAll('*').remove();

                        // If we don't pass any data, return out of the element
                        if (!data) return;

                        // setup variables
                        var width = d3.select(ele[0]).node().offsetWidth - margin,
                        // calculate the height
                            height = scope.data.length * (barHeight + barPadding),
                        // Use the category20() scale function for multicolor support
                            color = d3.scale.category20(),
                        // our xScale
                            xScale = d3.scale.linear()
                                .domain([0, d3.max(data, function (d) {
                                    return d.score;
                                })])
                                .range([0, width]);

                        // set the height based on the calculations above
                        svg.attr('height', height);

                        //create the rectangles for the bar chart
                        svg.selectAll('rect')
                            .data(data).enter()
                            .append('rect')
                            .attr('height', barHeight)
                            .attr('width', 140)
                            .attr('x', Math.round(margin / 2))
                            .attr('y', function (d, i) {
                                return i * (barHeight + barPadding);
                            })
                            .attr('fill', function (d) {
                                return color(d.score);
                            })
                            .transition()
                            .duration(1000)
                            .attr('width', function (d) {
                                return xScale(d.score);
                            });
                    }
                });
            }};
    }])

    .controller('d3graphCtrl', ['$scope', function ($scope) {
        var width = 960,
            height = 500;

        var x = d3.scale.linear()
            .range([0, width]);

        var y = d3.scale.linear()
            .range([0, height]);

        var color = d3.scale.category20c();

        var partition = d3.layout.partition()
            .children(function (d) {
                return isNaN(d.value) ? d3.entries(d.value) : null;
            })
            .value(function (d) {
                return d.value;
            });

        var svg = d3.select("body").append("svg")
            .attr("width", width)
            .attr("height", height);

        var rect = svg.selectAll("rect");

        d3.json("readme.json", function (error, root) {
            rect = rect
                .data(partition(d3.entries(root)[0]))
                .enter().append("rect")
                .attr("x", function (d) {
                    return x(d.x);
                })
                .attr("y", function (d) {
                    return y(d.y);
                })
                .attr("width", function (d) {
                    return x(d.dx);
                })
                .attr("height", function (d) {
                    return y(d.dy);
                })
                .attr("fill", function (d) {
                    return color((d.children ? d : d.parent).key);
                })
                .on("click", clicked);
        });

        function clicked(d) {
            x.domain([d.x, d.x + d.dx]);
            y.domain([d.y, 1]).range([d.y ? 20 : 0, height]);

            rect.transition()
                .duration(750)
                .attr("x", function (d) {
                    return x(d.x);
                })
                .attr("y", function (d) {
                    return y(d.y);
                })
                .attr("width", function (d) {
                    return x(d.x + d.dx) - x(d.x);
                })
                .attr("height", function (d) {
                    return y(d.y + d.dy) - y(d.y);
                });
        }
    }]);