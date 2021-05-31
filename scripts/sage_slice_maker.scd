Server.killAll();

(
s.waitForBoot({
    b = Buffer.read(s, "/Users/james/dev/webdev/phd-kit/static/ss/gesture.wav");
    s.sync;
    c = Buffer.new(s);

    FluidBufNoveltySlice.process(s, b, indices:c, action:{

        c.loadToFloatArray(action:{ | indices | ~indices = indices.as(Array) });

        s.sync;

        ~indices_desc = Array.newClear;

        ~indices.do({ | index, i |
            var color, next_index;
            if(i < (~indices.size - 1), {
                next_index = ~indices[i + 1]
            }, {
                next_index = b.numFrames
            });
            color = Color.rand(0.0, 1.0).hexString;
            ~indices[i] = [index, next_index, color];
            ~indices_desc = ~indices_desc.add((
                start: index,
                end: next_index,
                color: color
            ));
        });

        ~rand_indices = ~indices.scramble;

        ~final_array  = Array.newClear;

        ~rand_samples = Array.newClear;

        ~rand_indices.do({ | entry |
            var index = entry[0].asInteger;
            var next_index = entry[1].asInteger;
            var color = entry[2];
            b.loadToFloatArray(index, next_index - index, { | samples |
                ~rand_samples = ~rand_samples.add(samples);
            });

            ~final_array = ~final_array.add((
                start: index,
                end: next_index,
                color: color
            ));
        });

        s.sync;

        ~rand_samples = ~rand_samples.flatten;

        d = Buffer.loadCollection(s, ~rand_samples, b.numChannels);

        d.write("~/sage-shuffled.wav".standardizePath,"WAV","float");

        // Resort the ~rand_samples
        ~final_array.postln;

        // Write JSON

        g = File("~/pre.json".standardizePath, "w");
        g.write("{ \n");
        ~indices_desc.do({ |slice|
            ~s = slice.asString.replace("(", "{").replace(")", "}");
            g.write(~s + "," + "\n");
        });
        g.write("} \n");
        g.close();


/*        f = File("~/post.json".standardizePath,"w");
        f.write("{ \n");
        ~formatted.do({ |slice|
            ~s = slice.asString.replace("(", "{").replace(")", "}");
            f.write(~s + "," + "\n");
        });
        f.write("} \n");
        f.close();*/

    });
});
)