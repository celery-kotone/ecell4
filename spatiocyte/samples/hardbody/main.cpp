#include <string>

#include <ecell4/core/types.hpp>
#include <ecell4/core/Species.hpp>
#include <ecell4/core/Position3.hpp>
#include <ecell4/core/NetworkModel.hpp>

#include "../../SpatiocyteSimulator.cpp"

using namespace ecell4;
using namespace ecell4::spatiocyte;

/**
 * main function
 */
int main(int argc, char** argv)
{
    const Real L(1e-6);
    const Position3 edge_lengths(L, L, L);
    const Real volume(L * L * L);
    const Real voxel_radius(1e-8);
    const Integer N(60);

    const std::string D("1e-12"), radius("2.5e-9");

    const Real k2(0.1), U(0.5);
    const Real k1(k2 * volume * (1 - U) / (U * U * N));
    ecell4::Species sp1("A", D, radius), sp2("B", D, radius), sp3("C", D, radius);
    ReactionRule rr1(create_binding_reaction_rule(sp1, sp2, sp3, k1)),
        rr2(create_unbinding_reaction_rule(sp3, sp1, sp2, k2));

    boost::shared_ptr<ecell4::NetworkModel> model(new ecell4::NetworkModel());
    model->add_species(sp1);
    model->add_species(sp2);
    model->add_species(sp3);
    model->add_reaction_rule(rr1);
    model->add_reaction_rule(rr2);

    boost::shared_ptr<SpatiocyteWorld> world(
        new SpatiocyteWorld(edge_lengths, voxel_radius));
    // std::cout << "volume = " << volume << std::endl;
    // std::cout << "actual volume = " << world->volume() << std::endl;

    world->add_species(sp1);
    world->add_species(sp2);
    world->add_species(sp3);
    world->add_molecules(sp1, N / 2);
    world->add_molecules(sp2, N / 2);

    SpatiocyteSimulator sim(model, world);

    for (unsigned int i(0); i < 100; ++i)
    {
        sim.step();
    }

    std::cout << "t = " << sim.t() << std::endl;
    std::cout << "num_steps = " << sim.num_steps() << std::endl;
}